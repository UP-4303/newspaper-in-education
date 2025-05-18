import datetime
import asyncio

import gdelt.config as config
from gdelt.GdeltJsonGz import GdeltJsonGz

class GdeltConsumer:
    semaphore = asyncio.Semaphore(30)

    def __init__(self, session):
        self.session = session

    async def retrieveJsonGz(self, requestTime: datetime.datetime)-> GdeltJsonGz:
        async with self.semaphore:
            async with self.session.get(config.url(requestTime)) as response:
                content = await response.read()
        return GdeltJsonGz(content, requestTime)