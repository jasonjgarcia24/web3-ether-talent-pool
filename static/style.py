import streamlit as st


def set_style():
    st.markdown(
        """
        <style>
        p {
            color: #122221;
        }

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
            font-size: 16px;
            align-content: left;
        }

        .wage-text {
            font-size: 18px;
            margin: 5px 0 20px 0;
        }

        .candidate-info-header {
            font-size: 14px;
            text-align: left;
        }

        div.stMarkdown {
            margin: 0;
            padding: 0;
        }

        div.stButton {
            display: flex;
        }

        div.stButton > button:first-child {
            color: white;
            background: rgb(204, 49, 49);
            width: 170px;
            margin: 0 auto;
        }

        </style>
        """,

        unsafe_allow_html=True
    )

