#!/usr/bin/env python3
"""Implementing an expiring web cache and tracker """

from functools import wraps
import redis
import requests
from typing import Callable

r = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """count the request """

    @wraps(method)
    def wrapper(url):
        """ Wrapper function """
        r.incr(f"count:{url}")
        cached_html = r.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')

        html = method(url)
        r.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """Uses the requests module
    """
    req = requests.get(url)
    return req.text
