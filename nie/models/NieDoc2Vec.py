from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from gensim.utils import simple_preprocess
import numpy as np

import models.config as config
from models.VectorizerInterface import VectorizerInterface
from dataset import Dataset, Article

class NieDoc2Vec(VectorizerInterface):
    def __init__(self, model: Doc2Vec):
        self.model = model

    @classmethod
    def readCorpus(cls, article: Article, uId: int, forTraining: bool= False):
        corpusTokens = []
        for line in article.content:
            tokens = simple_preprocess(line)
            if forTraining:
                corpusTokens.append(TaggedDocument(tokens, [uId]))
            else:
                corpusTokens.append(tokens)
            uId+= 1
        return corpusTokens, uId

    @classmethod
    def readDataset(cls, dataset: Dataset, forTraining: bool= False):
        datasetTokens = []
        uId = 0
        for article in dataset:
            corpusTokens, uId = cls.readCorpus(article, uId, forTraining)
            datasetTokens.extend(corpusTokens)

        return datasetTokens
    
    def articleToVector(self, article: Article):
        return np.array([self.model.infer_vector(line) for line in self.__class__.readCorpus(article, 0)[0]])

    @classmethod
    def trainFromDataset(cls, dataset: Dataset, vectorSize= 100, epochs= 10):
        trainTokens = cls.readDataset(dataset, True)
        model = cls(Doc2Vec(workers= 16, vector_size= vectorSize, epochs= epochs))
        model.model.build_vocab(trainTokens)
        model.model.train(trainTokens, total_examples=model.model.corpus_count, epochs=model.model.epochs)
        return model
    
    def save(self, name: str, path=config.nieDoc2VecPath):
        self.model.save(path(name))
        return self

    @classmethod
    def load(cls, name: str, path=config.nieDoc2VecPath):
        this = cls(Doc2Vec.load(path(name)))
        return this