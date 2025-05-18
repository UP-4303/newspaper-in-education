import articleContent.config as config
from articleContent.ArticleContent import ArticleContent
from htmlParser import extractText

class ArticleRawContent:
    def __init__(self, data: str, id: str):
        self.obj = data
        self.id = id
        return
    
    def __getattr__(self, attr):
        return getattr(self.obj, attr)
    
    def save(self, path=config.rawFilePath)-> 'ArticleRawContent':
        with open(path(self.id), 'w', encoding='utf-8') as f:
            f.write(self.obj)
        return self

    @classmethod
    def load(cls, id, path=config.rawFilePath)-> 'ArticleRawContent':
        with open(path(id), 'r', encoding='utf-8') as f:
            this = cls(f.read(), id)
        return this
    
    def clean(self):
        paragraphs = extractText(self.obj)
        return ArticleContent(id= self.id, content= paragraphs, unusableTag= (paragraphs == []))
