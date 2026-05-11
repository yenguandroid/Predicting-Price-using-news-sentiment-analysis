# Predicting-Price-using-news-sentiment-analysis
This project focuses on two important analytical areas:

Exploratory analysis of financial news data
Quantitative analysis of stock market price data using technical indicators

The project combines financial news analysis with quantitative technical analysis to better understand relationships between news activity, market sentiment, and stock price behavior.
2. Objectives

The main objectives of this project are:

Task 1 Objectives
Perform exploratory data analysis (EDA) on financial news headlines
Analyze headline characteristics and publication behavior
Identify temporal publication patterns
Understand news distribution trends over time
Prepare cleaned and structured datasets for future sentiment analysis
Task 2 Objectives
Load and clean historical stock market datasets
Compute technical indicators using TA-Lib
Analyze stock market behavior using quantitative methods
Visualize stock trends and technical indicators
Compare market behavior across multiple technology companies
Build reusable and modular financial data analysis functions
# Task 1: Exploratory Data Analysis of Financial News
3.1 Data Preparation and Cleaning

The financial news dataset was initially loaded into a pandas DataFrame for preprocessing and exploratory analysis.

The following preprocessing steps were performed:

1. dataset loading missing value inspection
datetime conversion 
#load data
import pandas as pd

df = pd.read_csv("../data/raw/raw_analyst_ratings.csv")
df.head()  

2.  headline length computation
#Descriptive Statistics
#Headline Length
# Calculate headline length
df['headline_length'] = df['headline'].apply(len)

# Display descriptive statistics
headline_stats = df['headline_length'].describe()

print(headline_stats)
3. publication date analysis
# Publication Dates

# Convert date column to datetime
df['date'] = pd.to_datetime(
    df['date'],
    format='mixed',
    utc=True,
    errors='coerce'
)
4. feature extraction
#Text Analysis
#TF-IDF Keywords
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(stop_words='english', max_features=20)
X = vectorizer.fit_transform(df['headline'])

print(vectorizer.get_feature_names_out())

5. Count news articles by publication date
publication_counts = df['date'].dt.date.value_counts().sort_index()

print(publication_counts)
6. publishing hour extraction
import matplotlib.pyplot as plt

# Extract publishing hour
df['hour'] = df['date'].dt.hour

# Count publications by hour
hour_counts = df['hour'].value_counts().sort_index()

# Create larger figure
plt.figure(figsize=(12,6))

# Create bar plot
hour_counts.plot(kind='bar')

# Add labels and title
plt.title("Publishing Hour Distribution", fontsize=16)
plt.xlabel("Hour of Day", fontsize=12)
plt.ylabel("Number of Articles", fontsize=12)

# Rotate x-axis labels
plt.xticks(rotation=0)

# Add grid for readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()

The date column contained mixed timestamp formats and timezone inconsistencies. These issues were resolved using pandas datetime conversion with UTC standardization.
# Overall Task 1 Findings

The exploratory data analysis revealed:
1. strong growth in financial news activity
2. structured publishing behavior
3. meaningful temporal patterns
4. valuable opportunities for future sentiment analysis

The dataset was successfully cleaned and transformed into a reusable analytical format for future machine learning and sentiment modeling tasks.
# Task 2: Quantitative Financial Analysis Using TA-Lib and PyNance
Historical stock price datasets for the selected companies (Apple, Amazon, Google, Meta and Nevada) were loaded into pandas DataFrames.
import sys
import os

sys.path.append(os.path.abspath(".."))

# Add project root directory to Python path
from src.data_loader import load_and_clean_stock_data
aapl_df = load_and_clean_stock_data("../data/raw/AAPL.csv")

amzn_df = load_and_clean_stock_data("../data/raw/AMZN.csv")

goog_df = load_and_clean_stock_data("../data/raw/GOOG.csv")

meta_df = load_and_clean_stock_data("../data/raw/META.csv")

nvda_df = load_and_clean_stock_data("../data/raw/NVDA.csv")

 # #Import technical indcator Function in Notebook
import sys
import os

sys.path.append(os.path.abspath(".."))

from src.data_loader import load_and_clean_stock_data
from src.indicators import add_indicators   
#Load All Company Datasets
companies = {
    "AAPL": "../data/raw/AAPL.csv",
    "AMZN": "../data/raw/AMZN.csv",
    "GOOG": "../data/raw/GOOG.csv",
    "META": "../data/raw/META.csv",
    "NVDA": "../data/raw/NVDA.csv"
}

datasets = {}

for company, path in companies.items():
    datasets[company] = load_and_clean_stock_data(path)
# Apply Indicators to ALL Companies
for company in datasets:

    datasets[company] = add_indicators(datasets[company])    
# Reusable Python functions were developed to:

1. load datasets
2. clean missing values
3. convert date columns
4. standardize numeric columns
5. remove duplicates
6. sort observations chronologically
::data_loader.py
import pandas as pd


def load_and_clean_stock_data(file_path):
    """
    Load and clean stock price dataset.

    Parameters:
    -----------
    file_path : str
        Path to CSV stock dataset

    Returns:
    --------
    df : pandas.DataFrame
        Cleaned stock dataframe
    """

    # Load dataset
    df = pd.read_csv(file_path)

    # Standardize column names
    df.columns = df.columns.str.strip()

    # Convert Date column to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Sort by date
    df = df.sort_values('Date')

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df = df.dropna()

    # Ensure numeric columns are correct type
    numeric_cols = ['Open', 'High', 'Low', 'Close', 'Volume']

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Remove rows with invalid numeric values
    df = df.dropna()

    # Reset index
    df = df.reset_index(drop=True)

    return df
::and indcators.py
#Create Technical Indicator Functions
import talib


def add_indicators(df):

    # SMA
    df['SMA_20'] = talib.SMA(df['Close'], timeperiod=20)

    # EMA
    df['EMA_20'] = talib.EMA(df['Close'], timeperiod=20)

    # RSI
    df['RSI'] = talib.RSI(df['Close'], timeperiod=14)

    # MACD
    macd, macd_signal, macd_hist = talib.MACD(
        df['Close'],
        fastperiod=12,
        slowperiod=26,
        signalperiod=9
    )

    df['MACD'] = macd
    df['MACD_SIGNAL'] = macd_signal
    df['MACD_HIST'] = macd_hist

    return df


    # for applying technical_indicators for all copaniies such like:
    #Apply Indicators to ALL Companies
for company in datasets:

    datasets[company] = add_indicators(datasets[company])
# This modular structure improved:

1. code reusability
2. maintainability
3. scalability
# Verify Indicators Added for Apple
datasets["AAPL"][[
    'Close',
    'SMA_20',
    'EMA_20',
    'RSI',
    'MACD'
]].tail()
# Verify Indicators Added for Amazon
datasets["AMZN"][[
    'Close',
    'SMA_20',
    'EMA_20',
    'RSI',
    'MACD'
]].tail()
# Verify Indicators Added for Google
datasets["GOOG"][[
    'Close',
    'SMA_20',
    'EMA_20',
    'RSI',
    'MACD'
]].tail()
# Verify Indicators Added for META
datasets["META"][[
    'Close',
    'SMA_20',
    'EMA_20',
    'RSI',
    'MACD'
]].tail()
# Verify Indicators Added for NVDA
datasets["NVDA"][[
    'Close',
    'SMA_20',
    'EMA_20',
    'RSI',
    'MACD'
]].tail()
# Visualization for AAPL Price + Moving Averages
import matplotlib.pyplot as plt

aapl = datasets["AAPL"]
plt.figure(figsize=(14,6))

plt.plot(aapl['Date'], aapl['Close'], label='Close Price')
plt.plot(aapl['Date'], aapl['SMA_20'], label='SMA 20')
plt.plot(aapl['Date'], aapl['EMA_20'], label='EMA 20')

plt.title("AAPL Price with SMA and EMA", fontsize=16)

plt.xlabel("Date", fontsize=12)
plt.ylabel("Price (USD)", fontsize=12)

plt.legend()

plt.grid(True, linestyle='--', alpha=0.6)

plt.show()
## Insights from AAPL Price with SMA and EMA

1. Apple stock shows a strong long-term upward trend over the observed period.

2. The SMA and EMA lines closely follow the closing price, confirming consistent trend movement.

3. EMA reacts faster to short-term price fluctuations compared to SMA because it gives more weight to recent prices.

4. During periods of high volatility, the EMA adjusts more quickly than the SMA.

5. The moving averages help smooth noisy daily price fluctuations and reveal the overall market trend more clearly.

6. The sustained upward movement suggests long-term bullish momentum in AAPL stock performance.
#Visualization for AMAZON Price + Moving Averages
import matplotlib.pyplot as plt

amzn = datasets["AMZN"]

plt.figure(figsize=(14,6))

plt.plot(amzn['Date'], amzn['Close'], label='Close Price')
plt.plot(amzn['Date'], amzn['SMA_20'], label='SMA 20')
plt.plot(amzn['Date'], amzn['EMA_20'], label='EMA 20')

plt.title("AMAZON Price with SMA and EMA", fontsize=16)

plt.xlabel("Date", fontsize=12)
plt.ylabel("Price (USD)", fontsize=12)

plt.legend()

plt.grid(True, linestyle='--', alpha=0.6)

plt.show()
Overall Insights
1. Amazon demonstrates strong growth-oriented behavior.
2. EMA captures short-term volatility effectively.
3. SMA provides clearer long-term trend visibility.
4. The stock exhibits moderate-to-high volatility compared to traditional industries.
#Visualization for GOOGle Price + Moving Averages
import matplotlib.pyplot as plt

goog = datasets["GOOG"]

plt.figure(figsize=(14,6))

plt.plot(goog['Date'], goog['Close'], label='Close Price')
plt.plot(goog['Date'], goog['SMA_20'], label='SMA 20')
plt.plot(goog['Date'], goog['EMA_20'], label='EMA 20')

plt.title("Google Price with SMA and EMA", fontsize=16)

plt.xlabel("Date", fontsize=12)
plt.ylabel("Price (USD)", fontsize=12)

plt.legend()

plt.grid(True, linestyle='--', alpha=0.6)

plt.show()
Overall Insights
1. Google exhibits strong long-term stability.
2. The stock trend appears less erratic than highly speculative stocks.
3. Moving averages confirm sustained bullish momentum.
4. Technical indicators show stable trend continuation.
#Visualization for META Price + Moving Averages
import matplotlib.pyplot as plt

meta = datasets["META"]

plt.figure(figsize=(14,6))

plt.plot(meta['Date'], meta['Close'], label='Close Price')
plt.plot(meta['Date'], meta['SMA_20'], label='SMA 20')
plt.plot(meta['Date'], meta['EMA_20'], label='EMA 20')

plt.title("Meta Price with SMA and EMA", fontsize=16)

plt.xlabel("Date", fontsize=12)
plt.ylabel("Price (USD)", fontsize=12)

plt.legend()

plt.grid(True, linestyle='--', alpha=0.6)

plt.show()
Overall Insights
1. Meta exhibits higher short-term volatility.
2. EMA captures rapid market sentiment changes effectively.
3. SMA helps identify broader long-term direction.
4. Price behavior reflects investor sensitivity to technology-sector news.
#Visualization for NVDA Price + Moving Averages
import matplotlib.pyplot as plt

nvda = datasets["NVDA"]

plt.figure(figsize=(14,6))

plt.plot(nvda['Date'], nvda['Close'], label='Close Price')
plt.plot(nvda['Date'], nvda['SMA_20'], label='SMA 20')
plt.plot(nvda['Date'], nvda['EMA_20'], label='EMA 20')

plt.title("NVDA Price with SMA and EMA", fontsize=16)

plt.xlabel("Date", fontsize=12)
plt.ylabel("Price (USD)", fontsize=12)

plt.legend()

plt.grid(True, linestyle='--', alpha=0.6)

plt.show()
Overall Insights
1. NVIDIA exhibits the strongest growth momentum among major technology stocks.
2. High volatility accompanies rapid expansion.
3. EMA is particularly useful for tracking fast-moving price changes.
4. Technical indicators confirm strong market momentum and investor interest.
## Conclusion

The quantitative analysis successfully applied technical indicators to multiple technology company stock datasets. 

The results show that:
- all companies experienced long-term upward market trends,
- moving averages effectively smoothed price fluctuations,
- EMA reacted faster to recent price changes than SMA,
- technical indicators provided valuable insight into momentum and trend behavior.

Among the analyzed companies, NVIDIA and Meta exhibited higher volatility, while Apple and Google showed relatively more stable long-term growth patterns.

Overall, the analysis demonstrates the usefulness of TA-Lib indicators for understanding financial market behavior and supporting future predictive modeling tasks.