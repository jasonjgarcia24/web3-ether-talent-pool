import os

import streamlit.components.v1 as components
import streamlit as st


_NPM = False

if _NPM:
    _copycontent_button = components.declare_component(
        "copycontent-button",
        url="http://localhost:3001",
    )

else:
    root_dir  = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(root_dir, "frontend/build")

    _copycontent_button = components.declare_component(
        "copycontent_button",
        path=build_dir,
    )


def copycontent_button(
    str="Hello World!",
    lead_str="",
    copy_str="",
    href="#",
    key=None,
    font_size="12",
    font_weight="none",
    color="black",
    padding="0px",
    margin="0px",
    background="none"
):
    if not copy_str:
        copy_str = str

    return _copycontent_button(
        str=str,
        lead_str=lead_str,
        copy_str=copy_str,
        href=href,
        key=key,
        font_size=font_size,
        font_weight=font_weight,
        color=color,
        padding=padding,
        margin=margin,
        background=background,
    )


if not _NPM:
    st.title("Copy Content Button")

    style_kwargs = dict(
        font_size="72px",
        padding="0px",
        margin="0px",
        color="red",
    )

    _copycontent_button(
        str="hello Google!",
        lead_str="Well,",
        copy_str="You just successfully copied the string!",
        href="https://www.google.com/",
        **style_kwargs,
    )

