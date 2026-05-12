# STEP 4 — visualization.py: Create a separate and reusable visualization function
#Scatter Plot
import matplotlib.pyplot as plt


def plot_sentiment_vs_returns(
    df,
    company,
    correlation
):

    plt.figure(figsize=(10,6))

    plt.scatter(
        df['sentiment_score'],
        df['Daily_Return']
    )

    plt.title(
        f"{company}: Sentiment vs Daily Returns\nCorrelation = {correlation:.2f}"
    )

    plt.xlabel("Average Daily Sentiment")

    plt.ylabel("Daily Return (%)")

    plt.grid(True)

    plt.show()

    # Bar Chart

def plot_sentiment_category_returns(df, company):

     category_returns = (
        df.groupby('Sentiment_Category')['Daily_Return']
        .mean()
    )

     category_returns.plot(
        kind='bar',
        figsize=(8,5),
        title=f"{company}: Average Return by Sentiment Category"
    )

plt.ylabel("Average Daily Return (%)")

plt.grid(True)

plt.show()

