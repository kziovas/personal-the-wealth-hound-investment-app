import logging
from typing import Union

import streamlit as st
from yahoo_fin import stock_info

# Configure logging
logging.basicConfig(level=logging.INFO)


@st.cache_data(ttl=30)
def get_current_price(symbol: str) -> float:
    """
    Fetch the current live price for a stock or cryptocurrency from Yahoo Finance.

    This function uses the `yahoo_fin` library which is widely used in Python
    for real-time price fetching. Prices are cached for 30 seconds to reduce
    API calls and improve performance.

    Parameters:
    - symbol (str): The ticker symbol (e.g., 'AAPL', 'BTC-USD').

    Returns:
    - float: Current price of the asset. Returns 0.0 if there is an error.
    """
    try:
        # `get_live_price` returns a float-like value
        price: float = stock_info.get_live_price(symbol)
        logging.info(f"Fetched price for {symbol}: {price:.2f}")
        return float(price)
    except Exception as e:
        logging.error(f"Error fetching price for {symbol}: {e}")
        st.error(f"Error fetching price for {symbol}")
        return 0.0


def get_historical_prices(symbol: str, period: str = "1mo") -> Union[list, None]:
    """
    Fetch historical closing prices for a ticker from Yahoo Finance.

    Parameters:
    - symbol (str): The ticker symbol.
    - period (str): Time period for historical data (default: '1mo').

    Returns:
    - List of floats with closing prices, or None on error.
    """
    try:
        df = stock_info.get_data(symbol, interval="1d", start_date=None, end_date=None)
        prices = df["close"].tolist()
        logging.info(f"Fetched {len(prices)} historical prices for {symbol}")
        return prices
    except Exception as e:
        logging.error(f"Error fetching historical prices for {symbol}: {e}")
        return None
