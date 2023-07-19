#!/usr/bin/env python3

import redis
import uuid
from typing import Union, Callable

class Cache:
    """
    Cache class to store data in Redis with random keys.
    """
    def __init__(self) -> None:
        """
        Initializes the Cache and flushes the Redis database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the input data in Redis with a random key.

        Args:
            data: Data to be stored. Can be a str, bytes, int or float.

        Returns:
            str: The randomly generated key used to store the data in Redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        """
        Retrieves the value from Redis for the given key.

        Args:
            key: The key associated with the data in Redis.
            fn: A callable function to convert the data back to the desired format (Optional).

        Returns:
            Union[str, bytes, int, float]: The data retrieved from Redis, optionally converted using fn.
        """
        data = self._redis.get(key)
        if data is None:
            return None

        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        Retrieves the value from Redis for the given key and converts it to a UTF-8 string.

        Args:
            key: The key associated with the data in Redis.

        Returns:
            str: The data retrieved from Redis, converted to a UTF-8 string.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Retrieves the value from Redis for the given key and converts it to an integer.

        Args:
            key: The key associated with the data in Redis.

        Returns:
            int: The data retrieved from Redis, converted to an integer.
        """
        return self.get(key, fn=int)
