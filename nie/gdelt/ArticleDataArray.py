import datetime
import json
from pydantic import BaseModel, ConfigDict
from typing import List

import gdelt.config as config

class ArticleData(BaseModel):
    model_config = ConfigDict(frozen=True)
    
    id: str
    date: str
    url: str
    title: str

class ArticleDataArray:
    def __init__(self, data: List[ArticleData], date: datetime.datetime):

        if not all(isinstance(item, ArticleData) for item in data):
            raise TypeError("All items must be ArticleData instances")
        
        self._data = data
        self.date = date
        return
    
    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __delitem__(self, index):
        del self._data[index]

    def __len__(self):
        return len(self._data)
    
    def __iter__(self):
        return iter(self._data)

    def __getattr__(self, attr):
        return getattr(self._data, attr)
    
    def save(self, path=config.cleanFilePath)-> 'ArticleDataArray':
        with open(path(self.date), 'w', encoding='utf-8') as f:
            json.dump([articleData.model_dump() for articleData in self._data], f, indent= 4)
        return self

    @classmethod
    def load(cls, date, path=config.cleanFilePath)-> 'ArticleDataArray':
        with open(path(date), 'r', encoding='utf-8') as f:
            data = json.load(f)
            articles = [ArticleData.model_validate(item) for item in data]
        return cls(articles, date)