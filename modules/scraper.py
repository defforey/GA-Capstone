import csv
import datetime
import time
from contextlib import closing
from typing import List, Union

import requests
from requests import get
from requests.exceptions import RequestException
from tqdm import tqdm_notebook


def check_response_is_valid(resp: requests.models.Response) -> bool:
    """Assesses whether the response is valid or not.
    Returns True if the response seems to be HTML,
    False otherwise.

    Args:
        resp (requests.models.Response): Response object, which
        contains a server's response to an HTTP request.

    Returns:
        True or False, depending on whether the
        content type of the response if HTML/XML or
        otherwise.
    """
    content_type = resp.headers["Content-Type"].lower()
    return (
        resp.status_code == 200
        and content_type is not None
        and content_type.find("html") > -1
    )


def simple_get(url: str) -> Union[str, None]:
    """Attempts to get the content at `url` by making
    an HTTP GET request. If the content type of response
    is some kind of HTML/XML, return the text; otherwise
    return None.

    Args:
        url (str): website URL to be scraped

    Returns:
        Text from HTML/XML, None otherwise.
    """
    try:
        with closing(get(url)) as resp:
            if check_response_is_valid(resp):
                return resp.text
            else:
                return None

    except RequestException as e:
        print("Error during requests to {0} : {1}".format(url, str(e)))
        return None


def write_htmls_to_csv(books_list: List[int], path: str) -> str:
    """Attempt to get the content at the specified URL and write
    it to a csv file. Record pages that are scraped incorrectly.

    Args:
        book_list (List[int]): list of book IDs from the LibraryThing.
            These are used to find the right pages to scrape.
        path (str): location where the csv file is saved.

    Returns:
        The path where the raw scraped data is saved.
    """
    failed_book_ids = []
    timestamp = datetime.datetime.now().strftime("%y-%m-%dT%H:%M:%S")
    raw_htmls_path = f"{path}/scraped_raw_html_librarything_{timestamp}.csv"

    with open(raw_htmls_path, "w") as csv_file:
        fieldnames = ["book_id", "raw_html"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        # scrape book info!
        for book_id in tqdm_notebook(books_list):
            url = "https://www.librarything.com/work/{}".format(book_id)
            scraped_raw_html = simple_get(url)
            if scraped_raw_html is not None:
                writer.writerow({"book_id": book_id, "raw_html": scraped_raw_html})
            else:
                failed_book_ids.append(book_id)
            time.sleep(1)

        print(f"Pages scraped incorrectly: {failed_book_ids}")
    return raw_htmls_path
