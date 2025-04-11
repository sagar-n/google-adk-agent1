import yfinance as yf
import pandas as pd
import pandas_ta as ta
from google.adk.agents import Agent

def fetch_stock_data(ticker: str,period: str) -> str:
    try:
        stock = yf.Ticker(ticker)
        df = stock.history(period=period)
        if df.empty:
            return {"error": f"No data found for ticker symbol '{ticker}'."}

        # Ensure correct column names (if missing, set them)
        if list(df.columns) == list(range(len(df.columns))):  # unnamed numeric columns
            df.columns = ["Open", "High", "Low", "Close", "Volume", "Dividends", "Stock Splits"]

        df["Close"] = pd.to_numeric(df["Close"], errors="coerce")

        df.ta.sma(length=9, append=True)
        df.ta.rsi(length=14, append=True)

        latest = df.iloc[-1]
        sma = latest.get("SMA_9")
        rsi = latest.get("RSI_14")
        price = latest.get("Close")

        if pd.isna(sma) or pd.isna(rsi):
            return "Not enough data to compute indicators yet."

        trend = "uptrend" if price > sma else "downtrend"
        rsi_status = (
            "overbought" if rsi > 70 else "oversold" if rsi < 30 else "neutral"
        )

        return (
            f"The stock is in a {trend} with a 9-day SMA of ${sma:.2f}. "
            f"The RSI is {rsi:.2f}, indicating a {rsi_status} condition."
        )

    except Exception as e:
        return f"An error occurred during analysis: {str(e)}"

# Define the agent
root_agent = Agent(
    name="stock_analysis_agent",
    description=(
        "Fetches historical stock data and performs technical analysis using SMA and RSI.\n"
        "Provide the following inputs:\n"
        "• ticker (e.g., 'AAPL')\n"
        "• period (e.g., '3mo')\n"
        "The agent returns the start date, end date, 9-day Simple Moving Average (SMA), Relative Strength Index (RSI), and trend direction.\n"
        "Example call: fetch_stock_data('AAPL', '3mo')"
    ),
    tools=[fetch_stock_data],
    model="gemini-2.0-flash-exp",
)
