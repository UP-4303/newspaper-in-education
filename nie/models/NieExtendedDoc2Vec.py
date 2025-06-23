import numpy as np

from models.NieDoc2Vec import NieDoc2Vec
from dataset import Article
from CefrCsv import CefrCsv

class NieExtendedDoc2Vec(NieDoc2Vec):
    def articleToVector(self, article: Article):
        articleSentenceVectors = super().articleToVector(article)
        meanVector = self.weightedMean(articleSentenceVectors)

        cefrValues = np.array(list(CefrCsv.countCefr(article).values()))
        return [np.concatenate([meanVector, cefrValues])]
    
    def weightedMean(self, vectors: np.ndarray, weights: np.ndarray|None= None):
        if weights is None:
            return vectors.mean(axis=0)
        return np.average(vectors, axis=0, weights=weights)