def decide_trades(current_data, cash, holdings):
    """
    Mean-reversion strategy.

    Buys when price is meaningfully below its recent moving average.
    Sells when price is meaningfully above its recent moving average.
    """
    window = 20
    threshold = 0.03

    if len(current_data) < window:
        return {}

    decisions = {}
    latest = current_data.iloc[-1]

    for ticker, shares in holdings.items():
        price = latest[ticker]
        moving_average = current_data[ticker].tail(window).mean()
        deviation = price / moving_average - 1

        if deviation < -threshold and cash >= price:
            quantity = min(1.0, cash / price)
            decisions[ticker] = ("buy", quantity)

        elif deviation > threshold and shares > 0:
            quantity = min(1.0, shares)
            decisions[ticker] = ("sell", quantity)

    return decisions
