from typing import List
import json

import articleContent.config as config
from pydantic import BaseModel, ConfigDict

class ArticleContent(BaseModel):
    model_config = ConfigDict(frozen=True)
    
    id: str
    content: List[str]
    unusableTag: bool = False
    
    def __getattr__(self, attr):
        return getattr(self.content, attr)
    
    def save(self, path=config.cleanFilePath)-> 'ArticleContent':
        with open(path(self.id), 'w', encoding='utf-8') as f:
            json.dump(self.content, f, indent= 4)
        return self

    @classmethod
    def load(cls, id, path=config.cleanFilePath)-> 'ArticleContent':
        with open(path(id), 'r', encoding='utf-8') as f:
            content = json.load(f)
        this = cls.model_validate({'content': content, 'id': id, 'unusableTag': content == []})
        return this