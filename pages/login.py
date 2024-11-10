import time

import streamlit as st

from pages.footer import get_footer
from src.cookies import cookies

# Set page config
st.set_page_config(page_title="UzDavKarantin - Login", page_icon=":lock:")


def get_login(st: st) -> None:

    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login", type="primary"):
        if username == "admin" and password == "1":
            # first clear the cookie
            cookies["is_logged_in"] = "logged_in"
            cookies.save()
            st.success("Logged in as admin")
            st.balloons()
            time.sleep(0.5)
            st.switch_page("pages/home.py")
        else:
            st.error("Invalid username or password,  Please try again")


# call the function
get_login(st)
# Add footer
get_footer(st=st)
