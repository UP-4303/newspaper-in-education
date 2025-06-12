from abc import ABC, abstractmethod

from dataset import Article
from dataset import Dataset

class ClassifierInterface(ABC):
    @classmethod
    @abstractmethod
    def getLabels(self, dataset: Dataset):
        pass

    @abstractmethod
    def predict(self, article: Article):
        pass