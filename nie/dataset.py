import asyncio
import datetime
from typing import List
import pandas
from sklearn.neighbors import NearestNeighbors
import torch
from tqdm import tqdm
from tqdm.asyncio import tqdm_asyncio
import json
import readability
from pydantic import BaseModel, ConfigDict
from torch.utils.data import Dataset as TorchDataset
from transformers import AutoModel, AutoTokenizer

from gdelt.ArticleDataArray import ArticleData, ArticleDataArray
from articleContent.ArticleContent import ArticleContent
import asyncioConfig as asyncC
from articleContent.ArticleConsumer import ArticleConsumer
from gdelt.GdeltConsumer import GdeltConsumer
from htmlParser import splitIntoSentences
from models import ClassifierInterface
from requestsConfig import GetSession
from gdelt.config import formattedDate

datasetFolder = '../dataset/'
datasetPath = lambda name: datasetFolder + name

class ReadabilityGrades(BaseModel):
    model_config = ConfigDict(frozen=True)

    kincaid: float | None = None
    ari: float | None = None
    colemanLiau: float | None = None
    flesch: float | None = None
    gunningFog: float | None = None
    lix: float | None = None
    smogGrading: float | None = None
    rix: float | None = None
    daleChall: float | None = None
    
    @classmethod
    def fromReadability(cls, readabilityData):
        return cls(
            kincaid= readabilityData['Kincaid'],
            ari= readabilityData['ARI'],
            colemanLiau= readabilityData['Coleman-Liau'],
            flesch= readabilityData['FleschReadingEase'],
            gunningFog= readabilityData['GunningFogIndex'],
            lix= readabilityData['LIX'],
            smogGrading= readabilityData['SMOGIndex'],
            rix= readabilityData['RIX'],
            daleChall= readabilityData['DaleChallIndex']
        )

class SentenceInfo(BaseModel):
    model_config = ConfigDict(frozen=True)

    characters: int | None = None
    syllables: int | None = None
    words: int | None = None
    wordTypes: int | None = None
    sentences: int | None = None
    paragraphs: int | None = None
    
    charactersPerWord: float | None = None
    syllablesPerWord: float | None = None
    wordsPerSentence: float | None = None
    sentencePerParagraph: float | None = None
    typeTokenRatio: float | None = None
    
    longWords: int | None = None
    complexWords: int | None = None
    complexWordsDc: int | None = None

    shortSentences: int | None = None
    shortSentencesMostWords: int | None = None
    longSentences: int | None = None
    longSentencesLeastWords: int | None = None
    shortestSentence: int | None = None
    shortestSentenceIndex: int | None = None
    longestSentence: int | None = None
    longestSentenceIndex: int | None = None
    questions: int | None = None
    passiveSentences: int | None = None
    
    @classmethod
    def fromReadability(cls, readabilityData):
        return cls(
            characters= readabilityData['characters'],
            syllables= readabilityData['syllables'],
            words= readabilityData['words'],
            wordTypes= readabilityData['wordtypes'],
            sentences= readabilityData['sentences'],
            paragraphs= readabilityData['paragraphs'],

            charactersPerWord= readabilityData['characters_per_word'],
            syllablesPerWord= readabilityData['syll_per_word'],
            wordsPerSentence= readabilityData['words_per_sentence'],
            sentencePerParagraph= readabilityData['sentences_per_paragraph'],
            typeTokenRatio= readabilityData['type_token_ratio'],
            
            longWords= readabilityData['long_words'],
            complexWords= readabilityData['complex_words'],
            complexWordsDc= readabilityData['complex_words_dc']
        )

class WordUsage(BaseModel):
    model_config = ConfigDict(frozen=True)

    toBe: int | None = None
    auxiliary: int | None = None
    conjunctions: int | None = None
    pronouns: int | None = None
    prepositions: int | None = None
    nominalizations: int | None = None
    
    @classmethod
    def fromReadability(cls, readabilityData):
        return cls(
            toBe= readabilityData['tobeverb'],
            auxiliary= readabilityData['auxverb'],
            conjunctions= readabilityData['conjunction'],
            pronouns= readabilityData['pronoun'],
            prepositions= readabilityData['preposition'],
            nominalizations= readabilityData['nominalization']
        )
    
class SentenceBeginnings(BaseModel):
    model_config = ConfigDict(frozen=True)

    pronouns: int | None = None
    interrogativePronouns: int | None = None
    articles: int | None = None
    subordinations: int | None = None
    conjunctions: int | None = None
    prepositions: int | None = None

    @classmethod
    def fromReadability(cls, readabilityData):
        return cls(
            pronouns= readabilityData['pronoun'],
            interrogatives= readabilityData['interrogative'],
            articles= readabilityData['article'],
            subordinations= readabilityData['subordination'],
            conjunctions= readabilityData['conjunction'],
            prepositions= readabilityData['preposition']
        )

class ReadabilityScores(BaseModel):
    model_config = ConfigDict(frozen=True)

    readabilityGrades: ReadabilityGrades | None = None
    sentenceInfo: SentenceInfo | None = None
    wordUsage: WordUsage | None = None
    sentenceBeginnings: SentenceBeginnings | None = None

    @classmethod
    def fromReadability(cls, readabilityData):
        return cls(
            readabilityGrades= ReadabilityGrades.fromReadability(readabilityData['readability grades']),
            sentenceInfo= SentenceInfo.fromReadability(readabilityData['sentence info']),
            wordUsage= WordUsage.fromReadability(readabilityData['word usage']),
            sentenceBeginnings= SentenceBeginnings.fromReadability(readabilityData['sentence beginnings'])
        )
    
class ClearScores(BaseModel):
    model_config = ConfigDict(frozen=True)

    btEasiness: float
    btStandardError: float
    clearScore1: float
    clearScore2: float
    clearScore3: float
    clearScore4: float
    clearScore5: float
    clearScore6: float

class Article(BaseModel):
    model_config = ConfigDict(frozen=True)

    content: List[str]
    data: ArticleData | None = None
    readability: ReadabilityScores | None = None
    clearScores: ClearScores | None = None

class Dataset:
    session = GetSession()
    gdeltConsumer = GdeltConsumer.getConsumer(session)
    articleConsumer = ArticleConsumer.getConsumer(session)

    def __init__(self, data: List[Article]):

        if not all(isinstance(item, Article) for item in data):
            raise TypeError("All items must be Article instances")
        
        self._data = data
        return
    
    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __delitem__(self, index):
        del self._data[index]

    def __len__(self):
        return len(self._data)
    
    def __iter__(self):
        return iter(self._data)

    def __getattr__(self, attr):
        return getattr(self._data, attr)

    def save(self, name: str, path=datasetPath)-> 'Dataset':
        with open(path(name), 'w', encoding='utf-8') as f:
            json.dump([article.model_dump() for article in self._data], f, ensure_ascii=False, indent=4)
        return self

    @classmethod
    def load(cls, name: str, path=datasetPath) -> 'Dataset':
        with open(path(name), 'r', encoding='utf-8') as f:
            data = json.load(f)
            articles = [Article.model_validate(item) for item in data]
        return cls(articles)

    @classmethod
    def fromPartial(cls, dataArray: ArticleDataArray, contentArray: List[ArticleContent]) -> 'Dataset':
        articles = []
        for articleData, articleContent in zip(dataArray, contentArray):
            if not articleContent.unusableTag:
                articles.append(Article(
                    content= articleContent.content,
                    data= articleData,
                    readability= ReadabilityScores.fromReadability(readability.getmeasures('\n'.join(articleContent.content)))
                ))
        return cls(articles)
    
    @classmethod
    async def contentFromData(cls, articleData):
        return (await cls.articleConsumer.retrieveArticleContent(articleData)).clean()
    
    @classmethod
    async def partialFromDate(cls, targetDate: datetime.datetime):
        articleDataArray = (await cls.gdeltConsumer.retrieveJsonGz(targetDate)).uncompress().clean()
        
        if articleDataArray == []:
            return (articleDataArray, [])

        articleContentTaskArray = [asyncC.createTask(cls.contentFromData(articleData), name=f'article-{formattedDate(targetDate)}-{i}') for i, articleData in enumerate(articleDataArray)]

        partial = (articleDataArray, await asyncio.gather(*articleContentTaskArray))
        
        return partial
    
    @classmethod
    async def fromTargetDates(cls, targetDates: List[datetime.datetime]= [datetime.datetime(2020, 1, 1, h, m, 0) for h in range(24) for m in range(60)])-> 'Dataset':
        dataset = cls([])

        partialTaskArray = [asyncC.createTask(cls.partialFromDate(targetDate), name=f'gdelt-{formattedDate(targetDate)}') for targetDate in targetDates]

        partials = await tqdm_asyncio.gather(*partialTaskArray)
        
        for articleDataArray, articleContentArray in partials:
            dataset.extend(cls.fromPartial(articleDataArray, articleContentArray))
        print('download finished')
        dataset.save(f'../dataset/2020-01-01-{len(dataset)}.json')
        print('saved')
        return dataset
    
    @classmethod
    def fromClearCorpus(cls, path: str):
        clearCorpus = pandas.read_csv(path, sep= ',', header=0)

        articles = [Article(
            content=splitIntoSentences([row[0]]),
            clearScores= ClearScores(
                btEasiness= row[1],
                btStandardError= row[2],
                clearScore1= row[3],
                clearScore2= row[4],
                clearScore3= row[5],
                clearScore4= row[6],
                clearScore5= row[7],
                clearScore6= row[8]
            ),
            readability= ReadabilityScores(
                readabilityGrades= ReadabilityGrades(
                    kincaid= row[9]
                )
            )
        ) for row in clearCorpus[['Excerpt', 'BT Easiness', 'BT s.e.', 'firstPlace_pred', 'secondPlace_pred', 'thirdPlace_pred', 'fourthPlace_pred', 'fifthPlace_pred', 'sixthPlace_pred', 'Flesch-Kincaid-Grade-Level']].to_numpy()
        if row[2] != 0] # Likely to be an error

        dataset = cls(articles)
        return dataset
    
class TorchDatasetWrapper(TorchDataset):
    def __init__(self, dataset: List[str|List[str]], labels: List[int|float], weights: List[float], tokenizer):
        self.dataset = dataset
        self.labels = labels
        self.weights = weights
        self.tokenizer = tokenizer

        if not self.labels:
            self.regression = False
        else:
            self.regression = isinstance(self.labels[0], float)

    @classmethod
    def fromDataset(cls, dataset: Dataset, labels: List[int|float], tokenizer, weights: List[float] | None = None, splitAsSentences: bool= False):
        if not weights:
            weights = [1]*len(dataset)

        if splitAsSentences:
            extendedDataset = []
            extendedLabels = []
            extendedWeights = []
            for article, label, weight in zip(dataset, labels, weights):
                extendedDataset.extend(article.content)
                extendedLabels.extend([label]*len(article.content))
                extendedWeights.extend([weight]*len(article.content))
            this = cls(extendedDataset, extendedLabels, extendedWeights, tokenizer)
        else:
            this = cls([article.content for article in dataset], labels, weights, tokenizer)

        return this

    def addPseudoLabeledData(self, externalDataPath: str, trainedModel: ClassifierInterface, embeddingModelName: str= 'sentence-transformers/all-MiniLM-L6-v2', nNeighbors: int= 5):
        externalData = pandas.read_csv(externalDataPath, sep= ',', header=0)
        externalSentences = [sentence for row in externalData[['external_text']].to_numpy() if isinstance(row[0], str) for sentence in splitIntoSentences([row[0].replace('\n', ' ')])]
        
        tokenizer = AutoTokenizer.from_pretrained(embeddingModelName)

        if isinstance(self.dataset[0], list):
            labeledSentences = []
            for article in self.dataset:
                labeledSentences.extend(article)
        else:
            labeledSentences = self.dataset

        embeddingModel = AutoModel.from_pretrained(embeddingModelName)
        embeddingModel.eval()

        externalEmbeddings = []
        with torch.no_grad():
            for i in tqdm(range(len(externalSentences))):
                tokens = tokenizer(externalSentences[i], return_tensors="pt", padding=True, truncation=True, max_length=512)
                tokens = {k: v.to(embeddingModel.device) for k, v in tokens.items()}
                outputs = embeddingModel(**tokens)
                externalEmbeddings.append(outputs.last_hidden_state[:, 0, :])

        externalEmbeddings = torch.cat(externalEmbeddings).cpu().numpy()

        labeledEmbeddings = []
        with torch.no_grad():
            for i in tqdm(range(len(labeledSentences))):
                tokens = tokenizer(labeledSentences[i], return_tensors="pt", padding=True, truncation=True, max_length=512)
                tokens = {k: v.to(embeddingModel.device) for k, v in tokens.items()}
                outputs = embeddingModel(**tokens)
                labeledEmbeddings.append(outputs.last_hidden_state[:, 0, :])

        labeledEmbeddings = torch.cat(labeledEmbeddings).cpu().numpy()

        index = NearestNeighbors(n_neighbors=nNeighbors, metric='cosine')
        index.fit(labeledEmbeddings)

        indices = index.kneighbors(externalEmbeddings, n_neighbors=nNeighbors, return_distance=False)
        filtered = [externalSentences[i] for neighbors in indices for i in neighbors]

        for sentence in tqdm(filtered):
            if isinstance(self.dataset[0], list):
                self.dataset.append([sentence])
            else:
                self.dataset.append(sentence)
            self.labels.append(trainedModel.predictSentence(sentence))
            self.weights.append(0.5)
            
        return

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):
        text = self.dataset[idx]
        if isinstance(text, list):
            text = " ".join(text)
        encoding = self.tokenizer(text, truncation=True, padding='max_length', max_length=512)
        
        item = {key: torch.tensor(val) for key, val in encoding.items()}
        
        item['labels'] = torch.tensor(self.labels[idx], dtype=(torch.float if self.regression else torch.long))
        item['weights'] = torch.tensor(self.weights[idx], dtype=torch.float)
        
        return item
    
    def save(self, name: str, path=datasetPath)-> 'Dataset':
        with open(path(name), 'w', encoding='utf-8') as f:
            json.dump({'content': self.dataset, 'labels': self.labels, 'weights': self.weights}, f, ensure_ascii=False, indent=4)
        return self

    @classmethod
    def load(cls, name: str, tokenizer, path=datasetPath) -> 'Dataset':
        with open(path(name), 'r', encoding='utf-8') as f:
            data = json.load(f)
            dataset = data['content']
            labels = data['labels']
            weights = data['weights']
        this = cls(dataset, labels, weights, tokenizer)
        return this