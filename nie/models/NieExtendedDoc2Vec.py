import numpy as np
import pandas
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r"[A-Za-z]+\.(?:[A-Za-z]+\.)+|\w+")

from models.NieDoc2Vec import NieDoc2Vec
from dataset import Article

class CefrCsv:
    cefrDict = None

    @classmethod
    def getAsDict(cls):
        if cls.cefrDict == None:
            cefrCsv = pandas.read_csv('../cefrj.csv', sep=',', header=0)
            cls.cefrDict = dict(zip(cefrCsv['headword'], cefrCsv['CEFR']))
        return cls.cefrDict

class NieExtendedDoc2Vec(NieDoc2Vec):
    def articleToVector(self, article: Article):
        articleSentenceVectors = super().articleToVector(article)
        meanVector = self.weightedMean(articleSentenceVectors)

        cefrValues = np.array(list(self.countCefr(article).values()))
        return [np.concatenate([meanVector, cefrValues])]
    
    def weightedMean(self, vectors: np.ndarray, weights: np.ndarray|None= None):
        if weights is None:
            return vectors.mean(axis=0)
        return np.average(vectors, axis=0, weights=weights)
    
    def countCefr(self, article: Article):
        cefrDict = CefrCsv.getAsDict()

        retrieved = {
            'A1':0,
            'A2':0,
            'B1':0,
            'B2':0,
            'C1':0,
            'C2':0,
            'unknown':0
        }
        levels = set(retrieved.keys())

        for sentence in article.content:
            for token in tokenizer.tokenize(sentence.lower()):
                tokenLevel = cefrDict.get(token, 'unknown')
                if tokenLevel not in levels:
                    tokenLevel = 'unknown'
                retrieved[tokenLevel]+=1

        return retrieved