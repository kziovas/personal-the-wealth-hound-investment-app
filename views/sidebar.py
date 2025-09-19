import streamlit as st


def show_sidebar() -> str:
    """
    Render the sidebar and return the selected page name.

    Returns:
    - str: Selected page name
    """
    st.sidebar.image("assets/wealth_hound_icon.png", width=80)
    st.sidebar.title("Wealth Hound")
    page = st.sidebar.radio("Navigate", ["Personal Info", "Portfolio"])
    return page
