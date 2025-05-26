from sklearn import svm
import joblib
from tqdm import tqdm

import models.config as config
from dataset import Dataset, Article
from models.VectorizerInterface import VectorizerInterface
from models.ClassifierInterface import ClassifierInterface
import readabilityFormulas

class NieSVM(ClassifierInterface):
    def __init__(self, clf: svm.SVC, vectorizer: VectorizerInterface):
        self.clf = clf
        self.vectorizer = vectorizer
    
    @classmethod
    def trainFromDataset(cls, vectorizer: VectorizerInterface, dataset: Dataset):
        vectors = []
        classifications = []
        for article in tqdm(dataset):
            for vector in vectorizer.articleToVector(article):
                vectors.append(vector)
                classifications.append(readabilityFormulas.FleschLabel(article.readability.readabilityGrades.flesch))

        clf = svm.SVC()
        clf.fit(vectors, classifications)
        return cls(clf, vectorizer)
    
    def predict(self, article: Article):
        return self.clf.predict([line for line in self.vectorizer.articleToVector(article)])
    
    def save(self, name: str, path=config.nieSVMPath):
        joblib.dump(self.clf, path(name))
        return self

    @classmethod
    def load(cls, vectorizer: VectorizerInterface, name: str, path=config.nieSVMPath):
        this = cls(joblib.load(path(name)), vectorizer)
        return this