"""
My cool app for analyzing excel & csv files.
"""

import streamlit as st

from pages.config import get_st_config
from pages.footer import get_footer
from pages.sidebar import get_sidebar
from src.analyze import analyze_data
from src.cookies import cookies
from src.utils.load_data import change_column_type, load_data


def home_page(st):
    """
    This file contains the home page of the web app
    """

    # Sidebar
    uploaded_file, uploaded_spec = get_sidebar(st=st)

    # Main content
    st.title("Excel & CSV Analyzer")

    if uploaded_file:
        # Load data
        dfs = load_data(uploaded_file)
        # here select column and choose type for convert
        coumuns_list = dfs.columns
        st.write("Select column and choose type for convert:")
        column = st.selectbox("Select column", coumuns_list, key="column")
        type = st.selectbox(
            "Select type", ["datetime", "int", "float", "str"], key="type"
        )
        # Convert column type
        dfs = change_column_type(column, type, dfs)

        # Analyze data (uploaded_spec)
        analyze_data(dfs, uploaded_spec=None).explorer()


# set page config
st.set_page_config(**get_st_config())
# Get cookie
is_logged_in = cookies.get("is_logged_in")
if is_logged_in != "logged_in":
    st.switch_page("pages/login.py")
# call the function
home_page(st)
# Add footer
get_footer(st=st)
