#STEP 1 — sentiment_analysis.py: Create a separete and reusale Sentiment analyser function
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()


def get_sentiment_score(text):
    """
    Compute sentiment score using VADER.
    """

    score = sia.polarity_scores(str(text))

    return score['compound']


def classify_sentiment(score):
    """
    Convert sentiment score into category.
    """

    if score > 0.05:
        return "Positive"

    elif score < -0.05:
        return "Negative"

    return "Neutral"