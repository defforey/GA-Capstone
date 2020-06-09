import json
import re
from typing import List

import pandas as pd


def assess_problematic_entries(n_problems: int, data: List[dict]) -> None:
    """Calculate the percentage of entries in the dataset that
    could not be read.

    Args:
        n_problems (int): count of problematic entries
        data (List[dict]): dataset to be loaded
    """
    print(
        f"Problematic entries: {n_problems}/{len(data)}\
        ({100 * n_problems/len(data):3.1f}%)"
    )


def load_dataset(path: str) -> pd.DataFrame:
    """Load a dataset from a pseudo-JSON format into a
    dataframe using regular expressions.

    Args:
        path (str): location where file is stored

    Returns:
        The dataset read into a dataframe
    """
    with open(path) as f:
        data = []
        problems = 0
        for line_num, line in enumerate(f):
            try:
                # replace ' around keys/values with "
                cleaned_line = re.sub(r"(?<={|\s)'|'(?=,|:|})", '"', line)
                # replace all " in text with \"
                cleaned_line = re.sub(
                    r"(?<!{)(?<!,\s|:\s)\"(?!,|:|})", '\\"', cleaned_line
                )
                # replace all \' with '
                cleaned_line = cleaned_line.replace("\\'", "'")

                # removes rows where comments were incorrectly parsed as a key
                data_dict = json.loads(cleaned_line)
                for k in data_dict.keys():
                    assert len(k) < 20

                data.append(data_dict)
            except Exception:
                problems += 1
        assess_problematic_entries(n_problems=problems, data=data)
        return pd.DataFrame(data)


def format_dataframe(df: pd.DataFrame, column1: str, column2: str) -> pd.DataFrame:
    """ Remove unnecessary columns, rename some columns

    Args:
        df (pd.DataFrame): dataframe needing formatting

    Returns:
        Formatted dataframe
    """
    column1 = df.pop(column1)
    column2 = df.pop(column2)
    return df.rename(
        columns={"comment": "reviews", "nhelpful": "n_helpful", "work": "id"}
    )
