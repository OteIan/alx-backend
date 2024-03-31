#!/usr/bin/env python3
"""
Simple pagination
"""
import csv
import math
from typing import List, Dict


def index_range(page: int, page_size: int) -> tuple:
    """
    Helper function
    """
    return (page_size * (page - 1), page_size * page)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Simple pagination
        """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0

        start, end = index_range(page, page_size)

        data = self.dataset()

        if start > len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, int]:
        """
        Hypermedia Pagination
        """
        data = self.get_page(page, page_size)

        start, end = index_range(page, page_size)

        next_page = page + 1 if end + 1 < len(self.__dataset) else None
        prev_page = page - 1 if start - 1 > 0 else None

        return {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': math.ceil(len(self.__dataset) / page_size)
        }
