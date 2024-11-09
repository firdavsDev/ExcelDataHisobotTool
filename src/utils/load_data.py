import pandas as pd


def load_data(file) -> pd.DataFrame:
    """
    Load data from an excel or csv file.

    :param file: file object
    :return: pandas DataFrame
    """

    # split the file name and extension
    name, ext = file.name.split(".")
    # check if the file is an excel file
    if ext == "xlsx":
        dfs = pd.read_excel(file)
    # check if the file is a csv file
    elif ext == "csv":
        dfs = pd.read_csv(file)
    else:
        return None
    # return the dataframe
    return dfs
