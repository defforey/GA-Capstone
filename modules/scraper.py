from contextlib import closing
from typing import Union

import requests
from requests import get
from requests.exceptions import RequestException


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
