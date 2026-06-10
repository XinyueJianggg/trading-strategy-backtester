import numpy as np
import pandas as pd


def calculate_returns(portfolio_values: pd.Series) -> pd.Series:
    return portfolio_values.pct_change().dropna()


def cumulative_return(portfolio_values: pd.Series) -> float:
    return portfolio_values.iloc[-1] / portfolio_values.iloc[0] - 1


def annualized_return(portfolio_values: pd.Series, periods_per_year: int = 252) -> float:
    total_return = cumulative_return(portfolio_values)
    n_periods = len(portfolio_values) - 1
    if n_periods <= 0:
        return np.nan
    return (1 + total_return) ** (periods_per_year / n_periods) - 1


def annualized_volatility(returns: pd.Series, periods_per_year: int = 252) -> float:
    return returns.std() * np.sqrt(periods_per_year)


def sharpe_ratio(returns: pd.Series, risk_free_rate: float = 0.0, periods_per_year: int = 252) -> float:
    excess_returns = returns - risk_free_rate / periods_per_year
    vol = excess_returns.std()
    if vol == 0:
        return np.nan
    return excess_returns.mean() / vol * np.sqrt(periods_per_year)


def max_drawdown(portfolio_values: pd.Series) -> float:
    running_max = portfolio_values.cummax()
    drawdown = portfolio_values / running_max - 1
    return drawdown.min()


def historical_var(returns: pd.Series, confidence: float = 0.95) -> float:
    return -np.percentile(returns, 100 * (1 - confidence))


def historical_cvar(returns: pd.Series, confidence: float = 0.95) -> float:
    var_threshold = np.percentile(returns, 100 * (1 - confidence))
    tail_losses = returns[returns <= var_threshold]
    return -tail_losses.mean()


def summarize_strategy(portfolio_values: pd.Series) -> dict:
    returns = calculate_returns(portfolio_values)

    return {
        "Final Portfolio Value": portfolio_values.iloc[-1],
        "Cumulative Return": cumulative_return(portfolio_values),
        "Annualized Return": annualized_return(portfolio_values),
        "Annualized Volatility": annualized_volatility(returns),
        "Sharpe Ratio": sharpe_ratio(returns),
        "Max Drawdown": max_drawdown(portfolio_values),
        "Historical VaR 95%": historical_var(returns),
        "Historical CVaR 95%": historical_cvar(returns),
    }


def summarize_all_strategies(results: pd.DataFrame) -> pd.DataFrame:
    summaries = {}

    for col in results.columns:
        if col == "Date":
            continue
        summaries[col] = summarize_strategy(results[col])

    return pd.DataFrame(summaries).T
