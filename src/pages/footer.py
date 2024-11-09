# This file contains the footer of the web app
def get_footer(st):
    st.markdown(
        """
        <style>
            .footer {
                position: fixed;
                bottom: 0;
                left: 0;
                right: 0;
                padding: 10px;
                text-align: center;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p class="footer">Made with ❤️ by UzDavKarantin</p>', unsafe_allow_html=True
    )
