def decide_trades(current_data, cash, holdings):
    """
    Moving-average crossover strategy.

    Buys when short moving average is above long moving average.
    Sells when short moving average is below long moving average.
    """
    short_window = 5
    long_window = 20

    if len(current_data) < long_window:
        return {}

    decisions = {}
    latest = current_data.iloc[-1]

    for ticker, shares in holdings.items():
        short_ma = current_data[ticker].tail(short_window).mean()
        long_ma = current_data[ticker].tail(long_window).mean()
        price = latest[ticker]

        if short_ma > long_ma and cash >= price:
            quantity = min(1.0, cash / price)
            decisions[ticker] = ("buy", quantity)

        elif short_ma < long_ma and shares > 0:
            quantity = min(1.0, shares)
            decisions[ticker] = ("sell", quantity)

    return decisions
