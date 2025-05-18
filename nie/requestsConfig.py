import aiohttp
import asyncio
import signal
import atexit

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Referer": "https://www.google.com",
}

timeout = aiohttp.ClientTimeout(total=60)

cookie_jar = aiohttp.DummyCookieJar()

_session = None

def NewSession():
    global _session
    _session = aiohttp.ClientSession(headers= headers, timeout= timeout, cookie_jar=cookie_jar)

def IsEventLoopRunning():
    try:
        asyncio.get_running_loop()
        return True
    except RuntimeError:
        return False

async def AsyncNewSession():
    NewSession()
    
def GetSession():
    global _session
    if _session is None or _session.closed:
        if IsEventLoopRunning():
            NewSession()
        else:
            asyncio.run(AsyncNewSession())
    return _session

def CloseSession():
    global _session
    if _session and not _session.closed:
        if IsEventLoopRunning():
            asyncio.create_task(_session.close())
        else:
            loop = asyncio.new_event_loop()
            loop.run_until_complete(_session.close())
            loop.close()
        _session = None

def _signal_handler(sig, frame):
    CloseSession()
    raise KeyboardInterrupt

atexit.register(CloseSession)
signal.signal(signal.SIGINT, _signal_handler)
signal.signal(signal.SIGTERM, _signal_handler)