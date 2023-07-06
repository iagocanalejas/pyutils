import re


def split_money(value: str) -> tuple[str | None, float | None]:
    """
    Splits a money string into (currency, amount).
    Works with various formats like:
      - "$100"
      - "USD 100.50"
      - "100 EUR"
      - "€99.99"
      - "AUD1200.75"
    Returns:
      (currency: str | None, amount: float | None)
    """
    if not value or not isinstance(value, str):
        return None, None
    value = value.strip()

    pattern = re.compile(
        r"""
        ^\s*
        (?:
            (?P<currency_before>[^\d\s]+)\s*(?P<amount1>[\d,]+(?:\.\d+)?)
            |
            (?P<amount2>[\d,]+(?:\.\d+)?)\s*(?P<currency_after>[^\d\s]+)
        )
        \s*$
    """,
        re.VERBOSE,
    )

    match = pattern.match(value)
    if not match:
        return None, None

    currency = match.group("currency_before") or match.group("currency_after")
    amount_str = match.group("amount1") or match.group("amount2")

    try:
        amount = float(amount_str.replace(",", ""))
    except (ValueError, TypeError):
        amount = None

    return currency, amount


def symbol_to_currency(symbol: str) -> str | None:
    """
    Converts a currency symbol (e.g. "$", "€", "¥") or short form (e.g. "CA$", "A$")
    into a three-letter ISO 4217 currency code.

    Returns:
        The 3-letter currency code (e.g. "USD") or None if unknown.
    """
    if not symbol or not isinstance(symbol, str):
        return None

    symbol = symbol.strip().upper()

    mapping = {
        "$": "USD",
        "US$": "USD",
        "CA$": "CAD",
        "A$": "AUD",
        "NZ$": "NZD",
        "HK$": "HKD",
        "€": "EUR",
        "£": "GBP",
        "¥": "JPY",
        "₩": "KRW",
        "₹": "INR",
        "₽": "RUB",
        "₺": "TRY",
        "₫": "VND",
        "₴": "UAH",
        "₦": "NGN",
        "₪": "ILS",
        "R$": "BRL",
        "₱": "PHP",
        "CHF": "CHF",
        "CNY": "CNY",
        "JPY": "JPY",
        "AED": "AED",
        "SAR": "SAR",
        "ZAR": "ZAR",
    }

    # Exact match first
    if symbol in mapping:
        return mapping[symbol]

    # Handle symbols like "AUD$", "USD", etc.
    # Strip trailing '$' and check again
    if symbol.endswith("$"):
        possible = symbol[:-1]
        if possible in ["US", "CA", "AU", "NZ", "HK"]:
            return mapping.get(symbol, possible + "D")

    # If already 3 letters, assume it's a valid code
    if len(symbol) == 3 and symbol.isalpha():
        return symbol

    return None
