from src.cookies import cookies


def logout(st):
    st.write("Siz tizimdan chiqdingiz")
    cookies["is_logged_in"] = "not_logged_in"
    cookies.save()
    st.switch_page("pages/login.py")
