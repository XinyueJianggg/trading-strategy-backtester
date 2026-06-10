def decide_trades(current_data, cash, holdings):
    """
    Simple momentum strategy.

    Buys stocks with positive recent returns and sells stocks with negative recent returns.
    """
    lookback = 10

    if len(current_data) <= lookback:
        return {}

    decisions = {}
    latest = current_data.iloc[-1]
    previous = current_data.iloc[-lookback]

    for ticker, shares in holdings.items():
        price = latest[ticker]
        recent_return = latest[ticker] / previous[ticker] - 1

        if recent_return > 0.02 and cash >= price:
            quantity = min(1.0, cash / price)
            decisions[ticker] = ("buy", quantity)

        elif recent_return < -0.02 and shares > 0:
            quantity = min(1.0, shares)
            decisions[ticker] = ("sell", quantity)

    return decisions
