from sklearn.cluster import KMeans as scKMeans

from dataset import Dataset

class KMeans:
    @classmethod
    def getLabels(cls, dataset: Dataset, scoresFromArticle: function, randomState=0):
        scoreVectors = []
        for article in dataset:
            try:
                scores = scoresFromArticle(article)
                scoreVectors.append(scores)
            except Exception:
                continue

        kMeans = scKMeans(n_clusters=cls.nClusters, random_state=randomState)
        labels = kMeans.fit_predict(scoreVectors)
        
        return labels