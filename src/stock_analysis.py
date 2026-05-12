#STEP 2 — stock_analysis.py: Create a separate and reusable stock analyser functon
def calculate_daily_returns(df):
    """
    Calculate daily stock returns.
    """

    df = df.copy()

    df['Daily_Return'] = (
        df['Close'].pct_change() * 100
    )

    return df