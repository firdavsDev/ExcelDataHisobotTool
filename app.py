"""
My cool app for analyzing excel & csv files.
"""

import streamlit as st

from src.analyze import analyze_data
from src.pages.config import get_st_config
from src.pages.footer import get_footer
from src.pages.sidebar import get_sidebar
from src.utils.my_logger import set_up_logger

# Set up logger
logger = set_up_logger()

# Set up Streamlit page configuration
st_config = get_st_config()
st.set_page_config(**st_config)

# Sidebar
uploaded_file, uploaded_spec = get_sidebar(st=st)

# Main content
st.title("Excel & CSV Analyzer")

if uploaded_file:
    # Analyze data (uploaded_spec)
    analyze_data(uploaded_file, uploaded_spec=None).explorer()


# Footer in bottom of the page(st=st)
get_footer(st=st)
