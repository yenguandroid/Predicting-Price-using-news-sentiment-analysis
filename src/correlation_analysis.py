# STEP 3 — correlation_analysis.py: Create a separete and reusable coorrelation analyser function
import pandas as pd
from pandas.tseries.offsets import BDay


def align_to_trading_day(date):
    """
    Move weekend news to next business day.
    """

    if date.weekday() >= 5:
        return date + BDay(1)

    return date


def aggregate_daily_sentiment(news_df):
    """
    Compute average sentiment per trading day.
    """

    daily_sentiment = (
        news_df.groupby('trading_date')['sentiment_score']
        .mean()
        .reset_index()
    )

    return daily_sentiment


def merge_sentiment_and_returns(
    sentiment_df,
    stock_df
):
    """
    Merge sentiment data with stock returns.
    """

    stock_returns = stock_df[
        ['Date', 'Daily_Return']
    ]

    merged_df = pd.merge(
        sentiment_df,
        stock_returns,
        left_on='trading_date',
        right_on='Date',
        how='inner'
    )

    return merged_df