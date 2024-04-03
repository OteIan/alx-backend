#!/usr/bin/python3
"""
FIFO caching
"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Assigns items to the dictionary
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            poppedItem = self.cache_data.popitem(last=False)

            print(f"DISCARD: {poppedItem[0]}")

    def get(self, key):
        """
        Returns the value of key in the dictionary
        """
        return self.cache_data.get(key, None)
