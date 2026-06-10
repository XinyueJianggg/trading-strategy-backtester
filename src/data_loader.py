from pathlib import Path
import pandas as pd


def load_stock_data(data_dir: str | Path) -> pd.DataFrame:
    """
    Load stock CSV files from a folder and merge them into one price DataFrame.

    Each CSV should contain:
        Date, Price

    Returns:
        DataFrame with columns:
        Date, AAPL, MSFT, ...
    """
    data_dir = Path(data_dir)
    csv_files = sorted(data_dir.glob("*.csv"))

    if not csv_files:
        raise FileNotFoundError(f"No CSV files found in {data_dir}")

    merged = None

    for file_path in csv_files:
        ticker = file_path.stem
        df = pd.read_csv(file_path)

        if "Date" not in df.columns or "Price" not in df.columns:
            raise ValueError(f"{file_path.name} must contain Date and Price columns")

        df = df[["Date", "Price"]].rename(columns={"Price": ticker})
        df["Date"] = pd.to_datetime(df["Date"])

        if merged is None:
            merged = df
        else:
            merged = pd.merge(merged, df, on="Date", how="outer")

    merged = merged.sort_values("Date").reset_index(drop=True)
    return merged
