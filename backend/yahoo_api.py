import logging
from typing import List, Union

import streamlit as st
from yahoo_fin import stock_info

# Configure logging
logging.basicConfig(level=logging.INFO)


@st.cache_data(ttl=30)
def get_current_price(symbol: str) -> float:
    """
    Fetch the current live price for a stock or cryptocurrency from Yahoo Finance.

    Prices are cached for 30 seconds to reduce API calls.

    Parameters:
        symbol (str): Ticker symbol (e.g., 'AAPL', 'BTC-USD').

    Returns:
        float: Current price. Returns 0.0 if an error occurs.
    """
    try:
        price: float = stock_info.get_live_price(symbol)
        logging.info(f"Fetched price for {symbol}: {price:.2f}")
        return float(price)
    except Exception as e:
        logging.error(f"Error fetching price for {symbol}: {e}")
        return 0.0


@st.cache_data(ttl=3600)
def get_historical_prices(symbol: str, period: str = "1mo") -> Union[List[float], None]:
    """
    Fetch historical daily closing prices for a ticker from Yahoo Finance.

    Parameters:
        symbol (str): Ticker symbol.
        period (str): Time period (default: '1mo').

    Returns:
        List[float] or None: Closing prices or None if error occurs.
    """
    try:
        df = stock_info.get_data(symbol, interval="1d", start_date=None, end_date=None)
        prices = df["close"].tolist()
        logging.info(f"Fetched {len(prices)} historical prices for {symbol}")
        return prices
    except Exception as e:
        logging.error(f"Error fetching historical prices for {symbol}: {e}")
        return None
