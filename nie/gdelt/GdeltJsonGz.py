import datetime
import gzip

import gdelt.config as config
from gdelt.GdeltRawJson import GdeltRawJson

class GdeltJsonGz:
    def __init__(self, data: bytes, date: datetime.datetime):
        self.obj = data
        self.date = date
        return
    
    def __getattr__(self, attr):
        return getattr(self.obj, attr)

    def save(self, path=config.compressedFilePath)-> 'GdeltJsonGz':
        with open(path(self.date), 'wb') as f:
            f.write(self.obj)
        return self

    @classmethod
    def load(cls, date, path=config.compressedFilePath)-> 'GdeltJsonGz':
        with open(path(date), 'rb') as f:
            this = cls(f.read(), date)
        return this
    
    def uncompress(self)-> GdeltRawJson:
        return GdeltRawJson(gzip.decompress(self.obj).decode('utf-8'), self.date)