import streamlit as st

from backend import portfolio_logic
from backend.models import Asset
from backend.news_logic import get_latest_news
from views.layout import render_page_header


def render(asset: Asset):
    """
    Render detailed view of a single asset, including news and advisor tabs.

    Parameters:
    - asset: Asset ORM object
    """
    render_page_header(f"{asset.name} Details")

    # Fetch current price (cached)
    current_price = portfolio_logic.get_current_price(asset.name)

    # Get user base currency from asset's portfolio owner
    base_currency = asset.portfolio.owner.base_currency

    # Calculate profit/loss
    profit_asset, profit_base = portfolio_logic.calculate_profit_loss(
        asset, current_price, base_currency
    )

    st.subheader("Investment Details")
    st.markdown(
        f"- **Invested Amount:** {asset.invested_amount} {asset.invested_currency}"
    )
    st.markdown(
        f"- **Invested Price:** {asset.invested_price} {asset.invested_currency}"
    )
    st.markdown(f"- **Date Bought:** {asset.date_bought.strftime('%Y-%m-%d %H:%M:%S')}")
    st.markdown(f"- **Current Price:** {current_price:.2f} {asset.invested_currency}")

    st.markdown(
        f"**Profit/Loss ({asset.invested_currency}):** "
        f"{profit_asset:,.2f} {'🟢' if profit_asset >= 0 else '🔴'}"
    )
    st.markdown(
        f"**Profit/Loss ({base_currency}):** "
        f"{profit_base:,.2f} {'🟢' if profit_base >= 0 else '🔴'}"
    )

    # --- Tabs for News and Advisor ---
    tabs = st.tabs(["News", "Advisor"])

    # News tab
    with tabs[0]:
        news = get_latest_news(asset.id)
        st.info(news)

    # Advisor tab (placeholder)
    with tabs[1]:
        st.info(
            "Advisor tab coming soon: AI will suggest Buy/Hold/Sell based on user preferences."
        )
