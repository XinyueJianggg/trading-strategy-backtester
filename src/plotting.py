import matplotlib.pyplot as plt
import pandas as pd


def plot_portfolio_values(results: pd.DataFrame, output_path: str | None = None):
    plt.figure(figsize=(10, 6))

    for col in results.columns:
        if col != "Date":
            plt.plot(results["Date"], results[col], label=col)

    plt.title("Portfolio Value Comparison")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value")
    plt.legend()
    plt.tight_layout()

    if output_path:
        plt.savefig(output_path, dpi=300)

    plt.show()


def plot_drawdowns(results: pd.DataFrame, output_path: str | None = None):
    plt.figure(figsize=(10, 6))

    for col in results.columns:
        if col != "Date":
            running_max = results[col].cummax()
            drawdown = results[col] / running_max - 1
            plt.plot(results["Date"], drawdown, label=col)

    plt.title("Drawdown Comparison")
    plt.xlabel("Date")
    plt.ylabel("Drawdown")
    plt.legend()
    plt.tight_layout()

    if output_path:
        plt.savefig(output_path, dpi=300)

    plt.show()


def plot_return_distribution(results: pd.DataFrame, strategy_name: str, output_path: str | None = None):
    returns = results[strategy_name].pct_change().dropna()

    plt.figure(figsize=(8, 5))
    plt.hist(returns, bins=20)
    plt.title(f"Return Distribution: {strategy_name}")
    plt.xlabel("Daily Return")
    plt.ylabel("Frequency")
    plt.tight_layout()

    if output_path:
        plt.savefig(output_path, dpi=300)

    plt.show()
