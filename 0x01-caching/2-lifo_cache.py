#!/usr/bin/env python3
"""
LIFO Caching
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class
    """
    def __init__(self):
        super().__init__()
        self.last_key = ""

    def put(self, key, item):
        """
        Assigns items to a dictionary
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                del self.cache_data[self.last_key]
                print(f"DISCARD: {self.last_key}")

            self.last_key = key

    def get(self, key):
        """
        Returns the value of key
        """
        return self.cache_data.get(key, None)
