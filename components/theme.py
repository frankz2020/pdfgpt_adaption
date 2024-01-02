import streamlit as st

def theme() -> None:
    st.set_page_config(page_title="SmartIBD DocAI", page_icon="./static/img/favicon.ico", layout="centered")
    st.image('./static/img/logo.png', width=100)
