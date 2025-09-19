from typing import Tuple

import streamlit as st
from yahoo_fin import stock_info as si

from backend.models import Asset
from backend.yahoo_api import get_current_price as fetch_yahoo_price


def get_fx_rate(from_currency: str, to_currency: str) -> float:
    """
    Fetch the current exchange rate from `from_currency` to `to_currency` using Yahoo Finance.

    Example:
    - from_currency='EUR', to_currency='USD'

    Returns:
    - float: exchange rate
    """
    if from_currency == to_currency:
        return 1.0
    symbol = f"{from_currency}{to_currency}=X"  # Yahoo Finance FX ticker format
    try:
        rate = si.get_live_price(symbol)
        return float(rate)
    except Exception as e:
        st.warning(
            f"Could not fetch FX rate {from_currency}->{to_currency}, defaulting to 1.0: {e}"
        )
        return 1.0


def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
    """
    Convert amount from one currency to another using live FX rates from Yahoo Finance.
    """
    rate = get_fx_rate(from_currency, to_currency)
    return amount * rate


def calculate_profit_loss(
    asset: Asset, current_price: float, base_currency: str
) -> Tuple[float, float]:
    """
    Calculate profit/loss in asset currency and user's base currency.

    Returns:
    - Tuple[profit_in_asset_currency, profit_in_base_currency]
    """
    profit_asset = (current_price - asset.invested_price) * asset.invested_amount
    profit_base = convert_currency(profit_asset, asset.invested_currency, base_currency)
    return profit_asset, profit_base


def get_current_price(symbol: str) -> float:
    """
    Wrapper to fetch current price from Yahoo Finance.
    """
    return fetch_yahoo_price(symbol)
