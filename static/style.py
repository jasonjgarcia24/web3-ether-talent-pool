import streamlit as st


def set_style():
    st.markdown(
        """
        <style>
        .page-header {
            color: black;
            margin: 0;
            padding: 0px 0 20px 0;
            text-align: center;
            font-size: 64px;
            font-family: IBM Plex Sans,sans-serif;
        }

        .fintech-span {
            color: crimson;
        }

        .page-subheader {
            color: black;
            margin:0 0 20px 0;
            padding: 0px 0px 30px 0px;
            text-align:center;
            font-size: 32px;
            font-family: IBM Plex Sans,sans-serif;
            border-bottom: 1px solid #855555;
        }

        .professional-photo {
            height: 200px;
            width: 200px;
            border-radius: 15px;
            box-shadow: 0px 0px 0px 0px rgba(1, 1, 1, 0.9), 2px 2px 2px 0px rgba(1, 1, 1, 0.9);
        }

        .expander-p {
            color: #122221;
            font-size: 16px;
        }

        .wage-text {
            color: #122221;
            font-size: 22px;
            margin: 5px 0 20px 0;
        }

        div.stSelectbox {
        }

        div.stContainer {
            background: orange;
        }

        div.stButton > button:first-child {
            color: white;
            background-color: rgb(204, 49, 49);
        }

        </style>
        """,

        unsafe_allow_html=True
    )

