# %%
#%load_ext autoreload
#%autoreload 2
#%%
import datetime
import matplotlib.pyplot as plt
import asyncio
from tqdm.asyncio import tqdm_asyncio
from tqdm import tqdm
import numpy as np

import asyncioConfig as asyncC
from requestsConfig import GetSession
from gdelt.config import formattedDate
from gdelt.GdeltConsumer import GdeltConsumer
from gdelt.ArticleDataArray import ArticleDataArray
from articleContent.ArticleConsumer import ArticleConsumer
from articleContent.ArticleContent import ArticleContent
from dataset import Dataset
from models.NieDoc2Vec import NieDoc2Vec
from models.NieSVM import NieSVM
import readabilityFormulas

# %%
targetDate = datetime.datetime(2020, 1, 1, 0, 1, 0)
pathUncleanedTest1 = '../dataset/test1-uncleaned.json'
pathTest1 = '../dataset/test1.json'
pathUncleanedTest2 = '../dataset/test2-uncleaned.json'
pathTest2 = '../dataset/test2.json'
nieDoc2VecName = 'test2-0-6000'
nieSVMName = 'test2-0-6000'

session = GetSession()
gdeltConsumer = GdeltConsumer(session)
articleConsumer = ArticleConsumer(session)
asyncC.asyncioSetup()

def taskKiller():
    [task.cancel() for task in asyncio.all_tasks()]

# DATA FROM WEB
async def ArticleDataArrayFromWeb(targetDate):
    return await gdeltConsumer.retrieveJsonGz(targetDate).save().uncompress().save().clean().save()

# DATA FROM FILE
def ArticleDataArrayFromFile(targetDate):
    return ArticleDataArray.load(targetDate)

# CONTENT FROM WEB
async def ArticleContentArrayFromWeb(articleDataArray):
    return await tqdm_asyncio.gather(*[articleConsumer.retrieveArticleContent(articleData).save().clean().save() for articleData in articleDataArray])

# CONTENT FROM FILE
def ArticleContentArrayFromFile(articleDataArray):
    return [ArticleContent.load(articleData.id) for articleData in articleDataArray]

# DATASET FROM PARTIAL
def DatasetFromPartial(articleDataArray, articleContentArray):
    dataset = Dataset.fromPartial(articleDataArray, articleContentArray).save(pathUncleanedTest1)
    print(f'Dataset length uncleaned: {len(dataset)}')
    dataset = dataset.removeUnusableTagged().save(pathTest1)
    print(f'Dataset length cleaned: {len(dataset)}')
    return dataset

# DATASET FROM FILE
def DatasetFromFile():
    return Dataset.load(pathTest1)

async def ContentFromData(articleData):
    return (await articleConsumer.retrieveArticleContent(articleData)).clean()

async def PartialFromDate(targetDate):
    articleDataArray = (await gdeltConsumer.retrieveJsonGz(targetDate)).uncompress().clean()
    
    if articleDataArray == []:
        return (articleDataArray, [])

    articleContentTaskArray = [asyncC.createTask(ContentFromData(articleData), name=f'article-{formattedDate(targetDate)}-{i}') for i, articleData in enumerate(articleDataArray)]

    partial = (articleDataArray, await asyncio.gather(*articleContentTaskArray))
    
    return partial

# BIG DATASET
async def BigDataset():
    targetDates = [datetime.datetime(2020, 1, 1, h, m, 0) for h in range(24) for m in range(60)]

    dataset = Dataset([])

    partialTaskArray = [asyncC.createTask(PartialFromDate(targetDate), name=f'gdelt-{formattedDate(targetDate)}') for targetDate in targetDates]

    partials = await tqdm_asyncio.gather(*partialTaskArray)
    
    for articleDataArray, articleContentArray in partials:
        dataset.extend(Dataset.fromPartial(articleDataArray, articleContentArray))
    print('download finished')
    dataset.save(f'../dataset/2020-01-01-{len(dataset)}.json')
    print('saved')
    return dataset

def DatasetFromFile():
    datasetUnclean = Dataset.load(pathUncleanedTest2)
    dataset = Dataset.load(pathTest2)
    return (datasetUnclean, dataset)

def TrainingDataset(fromDataset, lineCount):
    trainingDataset = Dataset([])
    lines = 0
    i = 0
    while lines < lineCount and i < len(fromDataset):
        trainingDataset.append(fromDataset[i])
        lines+= len(fromDataset[i].content)
        i+=1
    return trainingDataset

# trainingDataset = dataset[:6000]
# testDataset = dataset[6000:]

def NieDoc2VecFromTraining(dataset):
    return NieDoc2Vec.trainFromDataset(dataset).save(nieDoc2VecName)

def NieDoc2VecFromFile():
    return NieDoc2Vec.load(nieDoc2VecName)

def NieSVMFromTraining(dataset, nieDoc2Vec):
    return NieSVM.trainFromDataset(nieDoc2Vec, dataset)

def NieSVMFromFile():
    return NieSVM.load(nieSVMName)

def Predict(dataset, nieSVM):
    correct = 0
    deviation = 0
    for article in tqdm(dataset):
        actual = readabilityFormulas.FleschLabel(article.readability.readabilityGrades.flesch)
        prediction = round(np.mean(nieSVM.predict(article)))
        if(prediction == actual):
            correct += 1
        deviation += abs(actual - prediction)
    print(f'Correct predictions {correct}/{len(dataset)}, {(correct/len(dataset))*100}%')
    print(f'Deviation {deviation}, average {deviation/len(dataset)}')

# %%
