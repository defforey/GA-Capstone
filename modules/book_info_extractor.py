import pandas as pd
from bs4 import BeautifulSoup


def extract_book_title(entry: str) -> str:
    """ Extracts a book title from a given HTML.

    Args:
        entry (str): text from HTML

    Returns:
        A string containing a book's title
    """
    try:
        return entry.find("div", attrs={"class": "headsummary"}).find("h1").text.strip()
    except Exception:
        return ""


def extract_book_author(entry: str) -> str:
    """ Extracts the name of the author of a book from a given HTML

    Args:
        entry (str): text from HTML

    Returns:
        A string containing the name of a book's author
    """
    try:
        return (
            entry.find("div", attrs={"class": "headsummary"})
            .find("h2")
            .text.strip()
            .replace("by ", "")
        )
    except Exception:
        return ""


def extract_book_isbn(entry: str) -> str:
    """ Extracts a book's International Standard Book Number (ISBN) from a given HMTL

    Args:
        entry (str): text from HTML

    Returns:
        A string containing a book's ISBN
    """
    try:
        return entry.find("div", attrs={"class": "description"}).find("h4").text.strip()
    except Exception:
        return ""


def extract_book_details(entry: str) -> pd.Series:
    """Passes entry into BeautifulSoup, then passes the output into three functions that
    extract book titles, author names and ISBNs from each HTML.

    Args:
        entry (str): text from HTML

    Returns:
        A pandas Series containing book titles, authors and ISBNs
    """
    soup = BeautifulSoup(entry, "html.parser")
    title = extract_book_title(soup)
    author = extract_book_author(soup)
    isbn = extract_book_isbn(soup)
    return pd.Series(data=[title, author, isbn], index=["book_title", "author", "isbn"])
