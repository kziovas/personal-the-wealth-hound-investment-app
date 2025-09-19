import streamlit as st


def render_page_header(page_title: str = ""):
    """
    Render a common top header for all pages with the app icon.

    Parameters:
    - page_title: Optional page-specific title
    """
    # Top bar with icon
    col1, col2 = st.columns([1, 8])
    with col1:
        st.image("assets/wealth_hound_icon.png", width=80)
    with col2:
        if page_title:
            st.markdown(f"## {page_title}")

    # Optional: add a horizontal line below header
    st.markdown("---")
