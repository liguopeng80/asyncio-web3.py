import lru
from urllib3.exceptions import HTTPError

import aiohttp


from web3.utils.caching import (
    generate_cache_key,
)


def _remove_session(key, session):
    session.close()


_session_cache = lru.LRU(8, callback=_remove_session)


def _get_session(*args, **kwargs):
    cache_key = generate_cache_key((args, kwargs))
    if cache_key not in _session_cache:
        _session_cache[cache_key] = aiohttp.ClientSession()
    return _session_cache[cache_key]


async def make_post_request(endpoint_uri, data, *args, **kwargs):
    kwargs.setdefault('timeout', 10)
    session = _get_session(endpoint_uri)

    async with session.post(endpoint_uri, data=data, **kwargs) as resp:
        http_error_msg = ''

        if 400 <= resp.status < 500:
            http_error_msg = u'%s Client Error: %s for url: %s' % (resp.status, resp.reason, endpoint_uri)

        elif 500 <= resp.status < 600:
            http_error_msg = u'%s Server Error: %s for url: %s' % (resp.status, resp.reason, endpoint_uri)

        if http_error_msg:
            raise HTTPError(http_error_msg)

        return await resp.read()

