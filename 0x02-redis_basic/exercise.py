#!/usr/bin/env python3
"""
Create a Cache class. In the __init__ method
"""

import redis
from uuid import uuid4
from typing import Callable, Optional, Union
from functools import wraps


def call_history(method: Callable) -> Callable:
    """ Create a store method that takes a data argument and returns a string"""
    method_sys = method.__qualname__
    input = method_sys + ':input'
    output = method_sys + ':output'

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """ wrapper function of redis """
        self._redis.rpush(input, str(args))
        data = method(self, *args, **kwds)
        self._redis.rpush(output, str(data))
        return data
    return wrapper


def count_calls(method: Callable) -> Callable:
    """ Create and return function that increments the count for that key"""
    method_sys = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """wrapped function """
        self._redis.incr(method_sys)
        return method(self, *args, **kwds)
    return wrapper




def replay(method: Callable):
    """Create a call history """
    method_sys = method.__qualname__
    inputs = method_sys + ":input"
    outputs = method_sys + ":output"
    redis = method.__self__._redis
    count = redis.get(method_sys).decode("utf-8")
    print("{} was call {} times:".format(method_sys, count))
    ListIn = redis.lrange(input, 0, -1)
    ListOut = redis.lrange(output, 0, -1)
    allData = list(zip(ListInput, ListOutput))
    for sys, data in allData:
        attr, data = sys.decode("utf-8"), data.decode("utf-8")
        print("{}(*{}) -> {}".format(method_sys, attr, data))


class Cache:
    """
    store information on redis
    """

    def __init__(self):
        """get the instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

        @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ storing list"""
        key = str(uuid4())
        self._redis.mset({key: data})
        return key

    def get(self,
            key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """ get the element"""
        data = self._redis.get(key)
        if (fn is not None):
            return fn(data)
        return data

    def get_str(self, data: str) -> str:
        """ return byte in string """
        return data.decode('utf-8')

    def get_int(self, data: str) -> int:
        """ return byte in integer """
        return int(data)
