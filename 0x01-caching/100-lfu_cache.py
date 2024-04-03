#!/usr/bin/env python3
"""
LFU Caching
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """
    LFUCache class
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()
        self.freq_keys = []

    def __reorder_items(self, lfu_key):
        """
        Ordered based on most recently used
        """
        max_positions = []
        lfu_freq = 0
        lfu_pos = 0
        ins_pos = 0

        for i, freq_key in enumerate(self.freq_keys):
            if freq_key[0] == lfu_key:
                lfu_freq = freq_key[1] + 1
                lfu_pos = i
                break
            elif len(max_positions) == 0:
                max_positions.append(i)
            elif freq_key[1] < self.freq_keys[max_positions[-1]][1]:
                max_positions.append(i)

        max_positions.reverse()
        for pos in max_positions:
            if self.freq_keys[pos][1] > lfu_freq:
                break
            ins_pos = pos

        self.freq_keys.pop(lfu_pos)
        self.freq_keys.insert(ins_pos, [lfu_key, lfu_freq])

    def put(self, key, item):
        """
        Assigns items to the dictionary
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lfu_key, _ = self.freq_keys[-1]
                self.cache_data.pop(lfu_key)
                self.freq_keys.pop()
                print(f"DISCARD: {lfu_key}")

            self.cache_data[key] = item
            idx = len(self.freq_keys)

            for i, freq_key in enumerate(self.freq_keys):
                if freq_key[1] == 0:
                    idx = i
                    break
            self.freq_keys.insert(idx, [key, 0])
        else:
            self.cache_data[key] = item
            self.__reorder_items(key)

    def get(self, key):
        """
        Returns the value of key
        """
        if key is not None and key in self.cache_data:
            self.__reorder_items(key)
        return self.cache_data.get(key, None)
