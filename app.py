"""
My cool app for analyzing excel & csv files.
"""

import streamlit as st

from src.cookies import cookies


# main function
def main(st: st) -> None:
    # check if user is logged in
    is_logged_in = cookies.get("is_logged_in")
    if is_logged_in == "logged_in":
        # switch to home page
        st.switch_page("pages/home.py")
    else:
        # switch to login page
        st.switch_page("pages/login.py")


if __name__ == "__main__":
    # Run the main function
    main(st=st)
