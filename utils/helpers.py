def format_currency(amount: float, currency: str) -> str:
    """
    Format a float amount with currency symbol.

    Parameters:
    - amount: float
    - currency: currency code

    Returns:
    - Formatted string
    """
    return f"{currency} {amount:,.2f}"


def color_profit_loss(amount: float) -> str:
    """
    Return a string with green for positive, red for negative.

    Parameters:
    - amount: float

    Returns:
    - str: Markdown formatted string
    """
    color = "green" if amount >= 0 else "red"
    return f"<span style='color:{color}'>{amount:,.2f}</span>"
