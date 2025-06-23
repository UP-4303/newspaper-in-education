from sklearn.cluster import KMeans as scKMeans

from dataset import Dataset

class KMeans:
    @classmethod
    def getLabels(cls, dataset: Dataset, nClusters, scoresFromArticle, randomState=0):
        scoreVectors = []
        for article in dataset:
            try:
                scores = scoresFromArticle(article)
                scoreVectors.append(scores)
            except Exception as e:
                # print(e)
                continue

        kMeans = scKMeans(n_clusters=nClusters, random_state=randomState)
        labels = kMeans.fit_predict(scoreVectors)
        
        return labels