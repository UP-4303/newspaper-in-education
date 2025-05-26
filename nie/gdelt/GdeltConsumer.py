import datetime
import asyncio

import gdelt.config as config
from gdelt.GdeltJsonGz import GdeltJsonGz

class GdeltConsumer:
    semaphore = asyncio.Semaphore(30)

    instances = {}

    def __init__(self, session):
        self.session = session

    async def retrieveJsonGz(self, requestTime: datetime.datetime)-> GdeltJsonGz:
        async with self.semaphore:
            async with self.session.get(config.url(requestTime)) as response:
                content = await response.read()
        return GdeltJsonGz(content, requestTime)
    
    @classmethod
    def getConsumer(cls, session):
        if not session in cls.instances:
            cls.instances[session] = cls(session)
        return cls.instances[session]