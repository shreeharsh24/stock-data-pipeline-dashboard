import yfinance as yf
import pandas as pd
from config import STOCK_SYMBOL


def extract():
    df = yf.download(
        STOCK_SYMBOL,
        period="1mo",
        interval="15m",
        auto_adjust=True,
        progress=False
    )
    print("Rows extracted:", len(df))
    return df


def transform(df):
    # 🔥 STEP 1: Flatten MultiIndex if exists
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    # 🔥 STEP 2: Convert index → column (VERY IMPORTANT)
    df = df.reset_index()

    # 🔥 STEP 3: Rename columns
    df = df.rename(columns={
        "Datetime": "date",
        "Date": "date",
        "Open": "open",
        "High": "high",
        "Low": "low",
        "Close": "close",
        "Volume": "volume"
    })

    # 🔥 STEP 4: Add symbol column
    df["symbol"] = STOCK_SYMBOL

    # 🔥 STEP 5: Select clean schema
    df = df[["symbol", "date", "open", "high", "low", "close", "volume"]]

    # 🔥 STEP 6: Drop duplicates (important for reruns)
    df = df.drop_duplicates(subset=["symbol", "date"])

    return df


def load(df, engine):
    df.to_sql(
        "stock_prices",
        engine,
        if_exists="append",
        index=False,
        method="multi"  # faster inserts
    )