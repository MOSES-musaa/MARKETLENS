import pandas as pd


def load_csv(file_path):
    """
    Reads a CSV file and returns a pandas DataFrame.
    """

    dataframe = pd.read_csv(file_path)
    dataframe.columns = dataframe.columns.str.lower()

    return dataframe