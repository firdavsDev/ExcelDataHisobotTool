# sidebar
def get_sidebar(st) -> tuple:
    st.sidebar.title("UzDavKarantin")
    st.sidebar.write(
        "Bu ilova orqali Excel va CSV fayllarni analiz qilishingiz mumkin."
    )
    # upload file on sidebar
    uploaded_file = st.sidebar.file_uploader(
        "Excel yoki CSV fayl yuklash", type=["xlsx", "csv"], key="file"
    )
    # upload spec on sidebar (optional)
    uploaded_spec = st.sidebar.file_uploader(
        "Spec fayl yuklash (agar mavjud bo'lsa)",
        type=["json"],
        key="spec",
        help="Spec fayl yuklash (agar mavjud bo'lsa)",
    )
    return uploaded_file, uploaded_spec
