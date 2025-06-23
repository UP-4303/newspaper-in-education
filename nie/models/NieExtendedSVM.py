from sklearn import svm
from tqdm import tqdm

from models.NieSVM import NieSVM
from models.VectorizerInterface import VectorizerInterface
from dataset import Dataset
from dataset import Article
from KMeans import KMeans

def scoresFromArticle(article: Article):
    return [
        article.clearScores.clearScore1,
        article.clearScores.clearScore2,
        article.clearScores.clearScore3,
        article.clearScores.clearScore4,
        article.clearScores.clearScore5,
        article.clearScores.clearScore6,
        article.readability.readabilityGrades.kincaid
    ]

class NieExtendedSVM(NieSVM):
    nClusters: int = 10

    @classmethod
    def getLabels(cls, dataset: Dataset):
        labels = KMeans.getLabels(dataset, cls.nClusters, scoresFromArticle)
        return labels

    @classmethod
    def trainFromDataset(cls, vectorizer: VectorizerInterface, dataset: Dataset, labels: list[int]):
        vectors = []
        classifications = []

        for i, article in enumerate(tqdm(dataset)):
            if labels[i] != None:
                for vector in vectorizer.articleToVector(article):
                    vectors.append(vector)
                    classifications.append(labels[i])

        clf = svm.SVC()
        clf.fit(vectors, classifications)
        return cls(clf, vectorizer)