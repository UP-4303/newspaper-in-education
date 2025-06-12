# %%
#%load_ext autoreload
#%autoreload 2
#%%
import datetime
import math
import matplotlib.pyplot as plt
from tqdm import tqdm
import numpy as np

import asyncioConfig as asyncC
from models.ClassifierInterface import ClassifierInterface
from requestsConfig import GetSession
from gdelt.GdeltConsumer import GdeltConsumer
from articleContent.ArticleConsumer import ArticleConsumer
from dataset import Dataset

# %%
# Dependencies setup
session = GetSession()
gdeltConsumer = GdeltConsumer.getConsumer(session)
articleConsumer = ArticleConsumer.getConsumer(session)
asyncC.asyncioSetup()

# Splits a dataset to have at least lineCount lines, rounded up by one article
def TrainingDataset(fromDataset: Dataset, lineCount: int):
    trainingDataset = Dataset([])
    lines = 0
    i = 0
    while lines < lineCount and i < len(fromDataset):
        trainingDataset.append(fromDataset[i])
        lines+= len(fromDataset[i].content)
        i+=1
    return trainingDataset

def Predict(dataset: Dataset, classifier: ClassifierInterface, labels: list[int]):
    correct = 0
    error = 0
    squaredError = 0
    for i, article in enumerate(tqdm(dataset)):
        actual = labels[i]
        if actual == None:
            continue
        prediction = round(np.mean(classifier.predict(article)))
        if(prediction == actual):
            correct += 1
        error += abs(actual - prediction)
        squaredError += abs(actual - prediction)**2
    print(f'Correct predictions {correct}/{len(dataset)}, {(correct/len(dataset))*100}%')
    print(f'Error {error}, mean error {error/len(dataset)}')
    print(f'Root Mean Square Error {math.sqrt(squaredError/len(dataset))}')

# %%
