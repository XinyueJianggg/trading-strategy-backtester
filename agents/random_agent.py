import random


def decide_trades(current_data, cash, holdings):
    """
    Random baseline agent.

    Randomly buys or sells up to one share of each stock.
    This is used as a naive benchmark.
    """
    latest = current_data.iloc[-1]
    decisions = {}

    for ticker, shares in holdings.items():
        price = latest[ticker]

        if random.random() < 0.5:
            quantity = min(1.0, cash / price)
            decisions[ticker] = ("buy", quantity)
        else:
            quantity = min(1.0, shares)
            decisions[ticker] = ("sell", quantity)

    return decisions
