import pandas as pd
import streamlit as st


def change_column_type(column_name, column_type, df):
    """
    Change the data type of a column.

    :param column_name: str
    :param column_type: str (e.g. "int64", "float64
    :param df: pandas DataFrame
    :return: pandas DataFrame
    """

    if column_type == "datetime":
        df[column_name] = pd.to_datetime(df[column_name], errors="coerce")
    else:
        df[column_name] = df[column_name].astype(column_type)

    return df


@st.cache_resource
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
        raise ValueError("File type not supported")
    # return the dataframe
    return dfs
