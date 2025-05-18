import datetime
import re
import json

import gdelt.config as config
from gdelt.ArticleDataArray import ArticleDataArray, ArticleData

class GdeltRawJson:
    def __init__(self, data: str, date: datetime.datetime):
        self.obj = data
        self.date = date
        return
    
    def __getattr__(self, attr):
        return getattr(self.obj, attr)
    
    def save(self, path=config.rawFilePath)-> 'GdeltRawJson':
        with open(path(self.date), 'w', encoding='utf-8') as f:
            f.write(self.obj)
        return self

    @classmethod
    def load(cls, date, path=config.rawFilePath)-> 'GdeltRawJson':
        with open(path(date), 'r', encoding='utf-8') as f:
            this = cls(f.read(), date)
        return this
    
    def clean(self)-> ArticleDataArray:
        # Make it all JSON
        gdeltJson = self.obj
        gdeltJson = '[' + gdeltJson + ']'
        gdeltJson = re.sub('\n{', ',{', gdeltJson)
        gdeltJson = re.sub('\\n', '', gdeltJson)

        jsonObject = json.loads(gdeltJson)

        articles = []
        for i in range(len(jsonObject)):
            article = jsonObject[i]

            articles.append(ArticleData(
                id= config.formattedDate(self.date) + '-' + str(i),
                date= article['date'],
                url= article['url'],
                title= article['title']
            ))
        return ArticleDataArray(articles, self.date)