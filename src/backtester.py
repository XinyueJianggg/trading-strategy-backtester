import pandas as pd


def run_backtest(price_data: pd.DataFrame, agent, initial_cash: float = 100000.0) -> pd.DataFrame:
    """
    Run a trading agent on historical price data.

    The agent must implement:
        decide_trades(current_data, cash, holdings)

    Returns:
        DataFrame with Date, Cash, StockValue, PortfolioValue.
    """
    tickers = [col for col in price_data.columns if col != "Date"]

    cash = initial_cash
    holdings = {ticker: 0.0 for ticker in tickers}
    history = []

    for i in range(len(price_data)):
        current_data = price_data.iloc[: i + 1]
        latest = current_data.iloc[-1]

        decisions = agent.decide_trades(current_data, cash, holdings.copy())

        for ticker, decision in decisions.items():
            if ticker not in tickers:
                continue

            action, quantity = decision
            quantity = max(float(quantity), 0.0)
            price = float(latest[ticker])

            if action == "buy":
                cost = price * quantity
                if cost <= cash:
                    cash -= cost
                    holdings[ticker] += quantity

            elif action == "sell":
                quantity = min(quantity, holdings[ticker])
                cash += price * quantity
                holdings[ticker] -= quantity

        stock_value = sum(float(latest[ticker]) * holdings[ticker] for ticker in tickers)
        portfolio_value = cash + stock_value

        history.append(
            {
                "Date": latest["Date"],
                "Cash": cash,
                "StockValue": stock_value,
                "PortfolioValue": portfolio_value,
            }
        )

    return pd.DataFrame(history)


def compare_agents(price_data: pd.DataFrame, agents: dict, initial_cash: float = 100000.0) -> pd.DataFrame:
    """
    Run multiple agents and return portfolio values in one DataFrame.
    """
    results = pd.DataFrame({"Date": price_data["Date"]})

    for name, agent in agents.items():
        backtest = run_backtest(price_data, agent, initial_cash)
        results[name] = backtest["PortfolioValue"]

    return results
