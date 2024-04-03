#!/usr/bin/python3
"""
Basic Dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Basic dictionary
    """
    def put(self, key, item):
        """
        Assigns to the dictionary
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value linked to key
        """
        try:
            return self.cache_data[key]
        except KeyError:
            return None
