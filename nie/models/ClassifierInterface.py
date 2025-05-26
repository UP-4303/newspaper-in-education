from abc import ABC, abstractmethod

from dataset import Article

class ClassifierInterface(ABC):
    @abstractmethod
    def predict(self, article: Article):
        pass