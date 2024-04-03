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
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Assigns items to a dictionary
        """
        if key is None and item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                poppedItem = self.cache_data.popitem(True)
                print(f"DISCARD: {poppedItem[0]}")

        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key, item):
        """
        Returns the value of key
        """
        return self.cache_data.get(key, None)
