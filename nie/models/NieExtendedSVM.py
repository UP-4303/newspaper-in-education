from sklearn import svm
from sklearn.cluster import KMeans
from tqdm import tqdm

from models.NieSVM import NieSVM
from models.VectorizerInterface import VectorizerInterface
from dataset import Dataset

class NieExtendedSVM(NieSVM):
    nClusters: int = 10

    @classmethod
    def getKMeans(cls, dataset: Dataset):
        scoreVectors = []
        for article in dataset:
            try:
                scores = [
                    article.clearScores.clearScore1,
                    article.clearScores.clearScore2,
                    article.clearScores.clearScore3,
                    article.clearScores.clearScore4,
                    article.clearScores.clearScore5,
                    article.clearScores.clearScore6,
                    article.readability.readabilityGrades.kincaid
                ]
                scoreVectors.append(scores)
            except Exception:
                continue

        kMeans = KMeans(n_clusters=cls.nClusters, random_state=0)
        labels = kMeans.fit_predict(scoreVectors)
        
        return labels

    @classmethod
    def trainFromDataset(cls, vectorizer: VectorizerInterface, dataset: Dataset, labels: list[int]):
        vectors = []
        classifications = []

        for i, article in enumerate(tqdm(dataset)):
            for vector in vectorizer.articleToVector(article):
                vectors.append(vector)
                classifications.append(labels[i])

        clf = svm.SVC()
        clf.fit(vectors, classifications)
        return cls(clf, vectorizer)