from abc import ABC, abstractmethod

from dataset import Article

class VectorizerInterface(ABC):
    @abstractmethod
    def articleToVector(self, article: Article):
        pass