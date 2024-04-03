#!/usr/bin/env python3
"""
LRU Caching
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class
    """
    def __init__(self):
        super().__init__()
        self.__usage = {}

    def put(self, key, item):
        """
        Assigns items to the dictionary
        """


    def get(self, key):
        """
        Returns the value of key
        """
        return self.cache_data.get(key, None)