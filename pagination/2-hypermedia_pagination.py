#!/usr/bin/env python3
"""Simple pagination module."""
import csv
import math
from typing import List, Dict, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple of the start and end index for pagination."""
    start = (page - 1) * page_size
    end = start + page_size
    return start, end


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns the correct page of the dataset."""

        # Validate arguments
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # Get the dataset
        dataset = self.dataset()

        # Use index_range to find the correct indices
        start, end = index_range(page, page_size)

        # Return the appropriate page, or an empty list
        if start >= len(dataset):
            return []

        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Returns a dictionary containing pagination info."""

        # Get the data for the current page
        data = self.get_page(page, page_size)

        # Calculate the total number of pages
        total_pages = math.ceil(len(self.dataset()) / page_size)

        # Determine the previous and next page numbers
        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < total_pages else None

        # Return a dictionary with pagination information
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
