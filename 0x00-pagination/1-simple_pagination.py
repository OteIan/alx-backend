#!/usr/bin/python3
"""
Simple pagination
"""
import csv
import math
from typing import List


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
        if not (isinstance(page, int) and isinstance(page_size, int)):
            raise AssertionError
        elif page <= 0 or page_size <= 0:
            raise AssertionError

        res = index_range(page, page_size)

        data = []

        with open(self.DATA_FILE, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for i, row in enumerate(csv_reader, start=1):
                if res[0] <= i <= res[1]:
                    data.append(row)
                elif i > res[1]:
                    break

        return data
