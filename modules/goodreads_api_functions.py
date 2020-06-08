import time
from typing import List

from betterreads import client
from requests import get
from tqdm import tqdm_notebook

gc = client.GoodreadsClient(
    "DOIHCwqd9wgM2dVm6827Og", "tWeUy3YeVrZ3a8E6rXjYLc3RvVhrM5zzHUNIdNMJBA"
)


def acquire_goodreads_id(isbn_numbers: List[str]) -> List[int]:
    """
    Collects Goodreads IDs using ISBNs and the Goodreads API. A 1 second delay
    is included in the function to avoid getting my IP address blocked.
    """
    goodreads_id = []
    for number in tqdm_notebook(isbn_numbers):
        base_url = "https://www.goodreads.com/book/isbn_to_id"
        params = {"key": "DOIHCwqd9wgM2dVm6827Og", "isbn": number}

        req_ = get(base_url, params=params)
        json_ = req_.json()
        goodreads_id.append(json_)
        time.sleep(1)
    return goodreads_id


def get_book_titles(book_id: List[int]) -> List[str]:
    book_titles = []
    for number in tqdm_notebook(book_id):
        book_titles.append((gc.book(number)).title)
        time.sleep(1)
    return book_titles


def get_book_shelves(book_id: List[int]) -> List[str]:
    book_shelves = []
    for number in tqdm_notebook(book_id):
        book_shelves.append((gc.book(number)).popular_shelves)
        time.sleep(1)
    return book_shelves