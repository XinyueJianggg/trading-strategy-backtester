_has_bought = False


def decide_trades(current_data, cash, holdings):
    """
    Buy-and-hold benchmark.

    On the first day, allocates cash equally across all stocks.
    After that, makes no trades.
    """
    global _has_bought

    if _has_bought:
        return {}

    latest = current_data.iloc[-1]
    tickers = list(holdings.keys())
    cash_per_stock = cash / len(tickers)

    decisions = {}

    for ticker in tickers:
        price = latest[ticker]
        quantity = cash_per_stock / price
        decisions[ticker] = ("buy", quantity)

    _has_bought = True
    return decisions
