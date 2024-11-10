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
                font-size: 16px;
                font-family: Arial, sans-serif;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <p class="footer">
        <b>
        Made with ❤️ by <a href="https://karantin.uz" target="_blank">UzDavKarantin</a>
        </b>
        </p>
        """,
        unsafe_allow_html=True,
    )
