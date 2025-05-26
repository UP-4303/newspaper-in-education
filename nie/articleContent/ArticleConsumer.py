import asyncio
import aiohttp
import aiofiles
from collections import defaultdict
import random

from gdelt.ArticleDataArray import ArticleDataArray, ArticleData
from articleContent.ArticleRawContent import ArticleRawContent

class ArticleConsumer:
    semaphore = asyncio.Semaphore(8192)
    semaphoreHost = defaultdict(lambda: asyncio.Semaphore(8))
    maxRetries = 3
    maxDelay = 30

    instances = {}
    
    def __init__(self, session: aiohttp.ClientSession, verbose: bool= False):
        self.session = session
        self.verbose = verbose
        open('error.txt', mode='w').close() # Empty the file on init

    def emptyArticleContent(self, id):
        return ArticleRawContent('', id)

    async def retrieveArticleContent(self, articleData: ArticleData):
        
        if articleData.url == '': # Yes, it does happen
            await self.log(f'{articleData.id}`{articleData.url}`, try0\nError: No URL')
            return self.emptyArticleContent(articleData.id)
        
        host = articleData.url.split('/')[2]
        attempt = 0
        retryAfter = 0
        content = ''
        inaccessible = False

        while attempt < self.maxRetries and content == '' and not inaccessible:

            # Exponential backoff + retryAfter + Anti Thundering Herd
            delay = (2 ** attempt) + retryAfter + random.uniform(0,1)
            await asyncio.sleep(min(delay, self.maxDelay))

            try:
                async with self.semaphoreHost[host]:
                    async with self.semaphore:
                        async with self.session.get(articleData.url) as response:

                            # Status OK
                            if response.status == 200:
                                content = await response.text()

                                # Status Unauthorized
                            elif response.status == 401:
                                inaccessible = True
                                await self.log(f'{articleData.id}`{articleData.url}`, try{attempt}\nError: 401 Unauthorized')
                            
                            # Status Forbidden
                            elif response.status == 403:
                                inaccessible = True
                                await self.log(f'{articleData.id}`{articleData.url}`, try{attempt}\nError: 403 Forbidden')

                            # Status Not Found
                            elif response.status == 404:
                                inaccessible = True
                                await self.log(f'{articleData.id}`{articleData.url}`, try{attempt}\nError: 404 Not Found')
                            
                            # Status Gone
                            elif response.status == 410:
                                inaccessible = True
                                await self.log(f'{articleData.id}`{articleData.url}`, try{attempt}\nError: 410 Gone')

                            # Status Too Many Requests
                            elif response.status == 429:
                                retryAfterHeader = response.headers.get('Retry-After')
                                if retryAfterHeader:
                                    retryAfter = int(retryAfterHeader)
                                    await self.log(f'{articleData.id}`{articleData.url}`, try{attempt}\nError: Will retry after {retryAfter}s')
                                else:
                                    await self.log(f'{articleData.id}`{articleData.url}`, try{attempt}\nError: Lacking RetryAfter header')
                           
                            # Other Status
                            else:
                                await self.log(f'{articleData.id}`{articleData.url}`, try{attempt}\nError: HTTP Status Code {response.status}')

            except UnicodeDecodeError as e: # Way too long, don't print it
                await self.log(f'{articleData.id}`{articleData.url}`, try{attempt}\nError: UnicodeDecodeError')
            except aiohttp.TooManyRedirects as e:
                await self.log(f'{articleData.id}`{articleData.url}`, try{attempt}\nError: TooManyRedirects')
            except TimeoutError as e:
                inaccessible = True # We have way to many timeouts to retry each one
                await self.log(f'{articleData.id}`{articleData.url}`, try{attempt}\nError: Timeout')
            except Exception as e:
                await self.log(f'{articleData.id}`{articleData.url}`, try{attempt}\nError: {repr(e)}')

            attempt+= 1
        
        # Max attempts reached
        if content != '':
            return ArticleRawContent(content, articleData.id)
        else:
            return self.emptyArticleContent(articleData.id)
    
    async def retrieveArticlesContent(self, articleDataArray: ArticleDataArray):
        return await asyncio.gather(*[self.retrieveArticleContent(gdeltData) for gdeltData in articleDataArray])
    
    async def log(self, message):
        if self.verbose:
            async with aiofiles.open('error.txt', mode='a') as f:
                await f.write(message + '\n')

    @classmethod
    def getConsumer(cls, session):
        if not session in cls.instances:
            cls.instances[session] = cls(session)
        return cls.instances[session]