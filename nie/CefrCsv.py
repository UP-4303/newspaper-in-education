import pandas
from nltk.tokenize import RegexpTokenizer

from dataset import Article

class CefrCsv:
    cefrDict = None
    tokenizer = RegexpTokenizer(r"[A-Za-z]+\.(?:[A-Za-z]+\.)+|\w+")

    @classmethod
    def getAsDict(cls, path: str='../cefrj.csv'):
        if cls.cefrDict == None:
            cefrCsv = pandas.read_csv(path, sep=',', header=0)
            cls.cefrDict = dict(zip(cefrCsv['headword'], cefrCsv['CEFR']))
        return cls.cefrDict
    
    @classmethod
    def countCefr(cls, article: Article):
        cefrDict = cls.getAsDict()

        retrieved = {
            'A1':0,
            'A2':0,
            'B1':0,
            'B2':0,
            'C1':0,
            'C2':0,
            'unknown':0
        }
        levels = set(retrieved.keys())

        for sentence in article.content:
            for token in cls.tokenizer.tokenize(sentence.lower()):
                tokenLevel = cefrDict.get(token, 'unknown')
                if tokenLevel not in levels:
                    tokenLevel = 'unknown'
                retrieved[tokenLevel]+=1

        return retrieved