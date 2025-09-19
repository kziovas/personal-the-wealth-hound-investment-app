import streamlit as st

from backend.db import SessionLocal
from backend.models import Asset
from views import asset_detail, personal_info, portfolio, sidebar

# --- App Configuration ---
st.set_page_config(
    page_title="Wealth Hound", page_icon="assets/wealth_hound_icon.png", layout="wide"
)

# --- Database session ---
db = SessionLocal()

# --- Check if user is logged in ---
if "user_id" not in st.session_state:
    # Show login/signup page first
    personal_info.render(db)
else:
    # --- Sidebar navigation ---
    page = sidebar.show_sidebar()

    # --- Page rendering logic ---
    if "selected_asset" in st.session_state:
        asset_id = st.session_state["selected_asset"]
        asset: Asset = db.query(Asset).get(asset_id)
        if asset:
            asset_detail.render(asset)
        else:
            st.error("Asset not found.")
    else:
        if page == "Personal Info":
            personal_info.render(db)
        elif page == "Portfolio":
            portfolio.render(db)
        else:
            st.write("Welcome to Wealth Hound! Select a page from the sidebar.")
