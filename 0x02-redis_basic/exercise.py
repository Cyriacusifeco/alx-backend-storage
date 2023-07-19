#!/usr/bin/env python3

import redis
import uuid
from typing import Union

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
