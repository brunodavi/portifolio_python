from functools import cache
import streamlit as st


def image_static(
        label: str,
        link: str,

        static_image: str = 'cat.png',

        width='',
        height='',
    ):

    return st.markdown(
        f'<a href="{link}">'
            '<img'
                f' src="app/static/{static_image}"'
                f' alt="{label}" width="{width}"'
                f' height="{height}">'
        '</a>',

        unsafe_allow_html=True
    )