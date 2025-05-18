from gdelt.ArticleDataArray import ArticleData, ArticleDataArray
from articleContent.ArticleContent import ArticleContent
from typing import List, Literal, OrderedDict
import json
import readability

from pydantic import BaseModel, ConfigDict

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

    readabilityGrades: ReadabilityGrades
    sentenceInfo: SentenceInfo
    wordUsage: WordUsage
    sentenceBeginnings: SentenceBeginnings

    @classmethod
    def fromReadability(cls, readabilityData):
        return cls(
            readabilityGrades= ReadabilityGrades.fromReadability(readabilityData['readability grades']),
            sentenceInfo= SentenceInfo.fromReadability(readabilityData['sentence info']),
            wordUsage= WordUsage.fromReadability(readabilityData['word usage']),
            sentenceBeginnings= SentenceBeginnings.fromReadability(readabilityData['sentence beginnings'])
        )

class Article(BaseModel):
    model_config = ConfigDict(frozen=True)

    content: List[str]
    data: ArticleData
    readability: ReadabilityScores

class Dataset:
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

    def save(self, path: str)-> 'Dataset':
        with open(path, 'w', encoding='utf-8') as f:
            json.dump([article.model_dump() for article in self._data], f, ensure_ascii=False, indent=4)
        return self

    @classmethod
    def load(cls, path: str) -> 'Dataset':
        with open(path, 'r', encoding='utf-8') as f:
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