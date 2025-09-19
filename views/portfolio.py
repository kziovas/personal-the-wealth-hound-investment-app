import streamlit as st
from sqlalchemy.orm import Session

from backend import portfolio_logic
from backend.models import Asset, Portfolio, User


def render(db: Session):
    """
    Render the portfolio page with asset list, add/delete functionality,
    and display total portfolio profit/loss.
    """
    st.title("Portfolio")

    if "user_id" not in st.session_state:
        st.warning("Please login first!")
        return

    user: User = db.query(User).get(st.session_state["user_id"])
    portfolios = user.portfolios

    # Create default portfolio if none exists
    if not portfolios:
        default_portfolio = Portfolio(name="Default Portfolio", owner=user)
        db.add(default_portfolio)
        db.commit()
        db.refresh(default_portfolio)
        portfolios = [default_portfolio]

    portfolio_names = [p.name for p in portfolios]
    selected_portfolio_name = st.selectbox("Select Portfolio", portfolio_names)
    selected_portfolio = next(
        (p for p in portfolios if p.name == selected_portfolio_name), None
    )

    if selected_portfolio:
        st.subheader(f"Assets in {selected_portfolio.name}")

        # --- Total Profit/Loss Calculation ---
        total_profit_asset = 0.0
        total_profit_base = 0.0
        for asset in selected_portfolio.assets:
            current_price = portfolio_logic.get_current_price(asset.name)
            profit_asset, profit_base = portfolio_logic.calculate_profit_loss(
                asset, current_price, user.base_currency
            )
            total_profit_asset += profit_asset
            total_profit_base += profit_base

        st.markdown(
            f"**Total Profit/Loss ({user.base_currency}):** "
            f"{total_profit_base:,.2f} {'🟢' if total_profit_base >= 0 else '🔴'}"
        )
        st.markdown(
            f"**Total Profit/Loss (per asset currency):** "
            f"{total_profit_asset:,.2f} {'🟢' if total_profit_asset >= 0 else '🔴'}"
        )

        # --- Add Asset Form ---
        with st.expander("Add New Asset"):
            with st.form("add_asset_form"):
                asset_name = st.text_input("Asset Name / Ticker")
                invested_amount = st.number_input("Invested Amount", min_value=0.0)
                invested_currency = st.selectbox("Currency", ["USD", "EUR", "GBP"])
                invested_price = st.number_input("Price per Unit", min_value=0.0)
                submitted = st.form_submit_button("Add Asset")
                if submitted:
                    new_asset = Asset(
                        name=asset_name,
                        invested_amount=invested_amount,
                        invested_currency=invested_currency,
                        invested_price=invested_price,
                        portfolio=selected_portfolio,
                    )
                    db.add(new_asset)
                    db.commit()
                    st.success(f"Added {asset_name} to {selected_portfolio.name}")
                    st.experimental_rerun()

        # --- Asset List with View and Delete ---
        for asset in selected_portfolio.assets:
            col1, col2, col3, col4, col5 = st.columns([3, 2, 2, 1, 1])
            with col1:
                st.markdown(f"**{asset.name}**")
            with col2:
                current_price = portfolio_logic.get_current_price(asset.name)
                st.write(f"{current_price:.2f} {asset.invested_currency}")
            with col3:
                profit_asset, profit_base = portfolio_logic.calculate_profit_loss(
                    asset, current_price, user.base_currency
                )
                st.write(
                    f"{profit_asset:,.2f} / {profit_base:,.2f} {user.base_currency}"
                )
            with col4:
                if st.button(f"View {asset.name}", key=f"view_{asset.id}"):
                    st.session_state["selected_asset"] = asset.id
                    st.experimental_rerun()
            with col5:
                if st.button("Delete", key=f"delete_{asset.id}"):
                    confirm = st.confirm(
                        f"Are you sure you want to delete {asset.name}?"
                    )
                    if confirm:
                        db.delete(asset)
                        db.commit()
                        st.success(f"{asset.name} deleted")
                        st.experimental_rerun()
