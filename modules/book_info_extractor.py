from typing import List, Tuple

import bs4
import pandas as pd
from bs4 import BeautifulSoup


def extract_book_title(entry: bs4.BeautifulSoup) -> str:
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


def extract_book_author(entry: bs4.BeautifulSoup) -> str:
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


def extract_book_isbn(entry: bs4.BeautifulSoup) -> str:
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


def clean_up_dataframe(df: pd.DataFrame, books_list: List[int]) -> pd.DataFrame:
    """Extract ISBNs using a regular expression, change
    data type to avoid losing leading zeroes, add book IDs
    and fill in missing information for a book missing its author.
    Remove books with missing ISBNs.

    Args:
        df (pd.DataFrame): dataframe containing book titles, authors
            and text containg IBSNs.
        books_list: list of book IDs

    Returns:
        A dataframe containg book IDs, titles, authors and ISBNs
    """
    df["isbn"] = df.isbn.str.extract(r"ISBN (\d+)\D", expand=False)
    df["id"] = books_list
    df = df[["id", "book_title", "author", "isbn"]].copy()
    df.author.iloc[4801] = "Jeremy Harmer"
    df.isbn.iloc[4801] = 9780521656139
    df = df.dropna().reset_index(drop=True)
    df["isbn"] = df.isbn.astype(str)
    return df


def generate_clean_isbn_and_id_lists(df: pd.DataFrame) -> Tuple[List[str], List[int]]:
    """Fix incorrect ISBN entries, remove those that
    are not 10 or 13 digits long. This will minimize
    errors when using the Goodreads API.

    Args:
        df (pd.DataFrame): dataframe containing book information
    Returns:
        A list of valid ISBNs and a list of LibraryThing
            book identifiers.
    """
    df.loc[df.book_title == "The Glass Castle", "isbn"] = "1844081826"
    df.loc[df.book_title == "Atonement (2001)", "isbn"] = "9780099429791"
    df.loc[df.book_title == "The Handmaid's Tale (1985)", "isbn"] = "9780385490818"
    df.loc[df.book_title == "Thirteen Reasons Why", "isbn"] = "0141328290"

    good_isbns = df[df.isbn.str.contains(r"^[\d]{10,13}$")].copy()
    good_isbns.isbn.iloc[284] = "9780060590284"
    good_isbns.isbn.iloc[441] = "9780060590284"
    good_isbns.isbn.iloc[1023] = "9780194790185"
    good_isbns.isbn.iloc[1906] = "9780515134506"
    good_isbns.isbn.iloc[2065] = "9780385536097"

    good_isbn_list = list(good_isbns.isbn)
    good_lbthing_id_list = list(good_isbns.id)
    return good_isbn_list, good_lbthing_id_list
