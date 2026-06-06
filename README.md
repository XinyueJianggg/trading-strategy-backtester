# Trading Strategy Backtester

A modular Python backtesting project for comparing simple multi-asset trading strategies with portfolio accounting, performance analytics, and downside risk metrics.

## Overview

This project is a cleaned and extended version of an educational trading-agent simulator. The original class framework allowed students to create trading agents, simulate trades using stock price data, and compare portfolio performance over time.

In this public-facing version, I reorganized the project into a more modular backtesting framework and added additional strategy agents, performance metrics, risk analytics, and visualizations.

The goal of this project is not to build a production trading system. Instead, it demonstrates how rule-based trading strategies can be evaluated under a consistent portfolio-accounting framework.

## Project Motivation

Simple trading strategies can look attractive if they are judged only by final portfolio value. A more complete evaluation should also consider volatility, drawdowns, and downside tail risk.

This project compares several basic trading agents and evaluates them using both return-based and risk-based metrics.

## Strategies Implemented

The project compares the following strategies:

- Random trading baseline
- Buy-and-hold benchmark
- Moving-average crossover strategy
- Momentum strategy
- Mean-reversion strategy

Each strategy follows the same agent interface:

```python
def decide_trades(current_data, cash, holdings):
    ...
````

This makes it easy to add new strategies and compare them under the same simulation engine.

## Features

* Multi-asset portfolio backtesting
* Cash and holdings tracking
* Rule-based trading agents
* Portfolio value simulation over time
* Strategy comparison table
* Performance and risk metrics
* Portfolio value visualization
* Drawdown visualization
* Return distribution visualization

## Performance Metrics

The project evaluates each strategy using:

* Final portfolio value
* Cumulative return
* Annualized return
* Annualized volatility
* Sharpe ratio
* Maximum drawdown
* Historical Value at Risk, VaR
* Historical Conditional Value at Risk, CVaR

## Repository Structure

```text
trading-strategy-backtester/
│
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
│
├── data/
│   └── stocks/
│       ├── AAPL.csv
│       ├── AMD.csv
│       ├── AMZN.csv
│       ├── BABA.csv
│       ├── GOOG.csv
│       ├── INTC.csv
│       ├── META.csv
│       ├── MSFT.csv
│       ├── NFLX.csv
│       ├── NVDA.csv
│       ├── TSLA.csv
│       └── V.csv
│
├── agents/
│   ├── __init__.py
│   ├── random_agent.py
│   ├── buy_and_hold_agent.py
│   ├── moving_average_agent.py
│   ├── momentum_agent.py
│   └── mean_reversion_agent.py
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── backtester.py
│   ├── metrics.py
│   └── plotting.py
│
├── notebooks/
│   └── trading_strategy_showcase.ipynb
│
└── outputs/
    ├── strategy_summary.csv
    ├── portfolio_values.csv
    └── figures/
        ├── portfolio_value_comparison.png
        ├── drawdown_comparison.png
        └── return_distribution.png
```

## How to Run

Clone the repository:

```bash
git clone https://github.com/XinyueJianggg/trading-strategy-backtester.git
cd trading-strategy-backtester
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Open the showcase notebook:

```bash
jupyter notebook notebooks/trading_strategy_showcase.ipynb
```

## Example Workflow

The main notebook follows this workflow:

1. Load stock price data from CSV files.
2. Define several trading agents.
3. Run each agent through the same backtesting engine.
4. Track cash, holdings, and portfolio value over time.
5. Compare strategies using risk and return metrics.
6. Generate visualizations for portfolio value, drawdowns, and return distributions.

## Sample Output

The project generates:

```text
outputs/portfolio_values.csv
outputs/strategy_summary.csv
outputs/figures/portfolio_value_comparison.png
outputs/figures/drawdown_comparison.png
outputs/figures/return_distribution.png
```

These outputs make it possible to inspect strategy performance without rerunning the full notebook.

## Interpretation

The strategy comparison shows that final portfolio value alone is not enough to evaluate a trading strategy. A strategy may end with a higher value but also experience larger drawdowns or higher volatility.

The added risk metrics provide a more complete comparison:

* Sharpe ratio measures return per unit of volatility.
* Maximum drawdown captures peak-to-trough portfolio loss.
* VaR estimates downside loss at a selected confidence level.
* CVaR estimates the average loss in the downside tail.

Because this project uses simplified strategies and sample price data, the results should be interpreted as a backtesting demonstration rather than investment advice.

## Limitations

This project is intentionally simplified. Current limitations include:

* No transaction costs or bid-ask spreads
* No market impact modeling
* No short selling
* No leverage
* No dividend adjustments
* No survivorship-bias treatment
* Limited sample data
* Simple rule-based strategies only

Future extensions could include transaction costs, position limits, real historical market data, benchmark comparison, walk-forward validation, and more advanced strategy classes.

## Attribution

This project was inspired by and partially adapted from the educational **Trading Agent Simulator** framework created by Zheng Cao for the Johns Hopkins University Financial Mathematics Master's 2025 Winter Intersection course.

The original framework introduced the idea of loading trading agents, simulating trades across stock price data, and ranking agents by portfolio value. I reorganized and extended the framework into a public-facing backtesting project by adding modular code, additional strategies, risk metrics, visualizations, and a showcase notebook.

Original repository:

```text
https://github.com/WashingtonHusky/Trading_Agent_Simulator
```

Citation requested by the original project:

```text
Cao, Z., "Trading Agent Simulation and Stock Simulator Framework," GitHub repository,
https://github.com/WashingtonHusky/Trading_Agent_Simulator.
```

The original README states that the project is licensed under the MIT License and asks users to cite the author when using the code in academic work. This repository keeps attribution clear and uses the original class framework only as an educational starting point. 

## Disclaimer

This project is for educational and portfolio demonstration purposes only. It is not financial advice, investment advice, or a production trading system.
