import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager


def get_cookie():
    cookies = EncryptedCookieManager(
        # This prefix will get added to all your cookie names.
        # This way you can run your app on Streamlit Cloud without cookie name clashes with other apps.
        prefix="my_app_",
        # You should really setup a long COOKIES_PASSWORD secret if you're running on Streamlit Cloud.
        password="my_secret_password",
    )
    if not cookies.ready():
        # Wait for the component to load and send us current cookies.
        st.stop()

    return cookies


# Get cookie
cookies = get_cookie()
# logged_in = cookies.get("is_logged_in")
