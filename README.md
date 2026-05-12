
# Executive Summary
Financial markets are highly sensitive to information. News headlines, analyst ratings, earnings announcements, and macroeconomic events can influence investor sentiment and potentially affect stock price movement. This project investigates whether financial news sentiment has a measurable relationship with daily stock returns for five major technology companies: Apple (AAPL), Amazon (AMZN), Google (GOOG), Meta (META/FB), and NVIDIA (NVDA).
The project combines Natural Language Processing (NLP), financial technical analysis, time-series analysis, and statistical correlation methods to analyze both stock market behavior and financial news sentiment.
Three major tasks were completed throughout the project:
1.	Exploratory Data Analysis (EDA) on the financial news dataset
2.	Quantitative stock analysis using TA-Lib technical indicators
3.	Correlation analysis between news sentiment and stock price movement
The analysis revealed that although some companies showed weak positive relationships between sentiment and daily returns, sentiment alone was not a strong predictor of short-term stock performance. Technical indicators provided clearer insights into market momentum, trend reversals, and volatility behavior.
The project demonstrates how financial NLP and quantitative analysis techniques can be integrated into a complete data science workflow.
Introduction
Financial news has become one of the most influential sources of information in modern stock markets. Investors, institutions, and algorithmic trading systems continuously analyze news content to estimate market sentiment and identify potential investment opportunities.
At the same time, technical analysis remains one of the most commonly used approaches for understanding stock market behavior. Indicators such as Moving Averages, RSI, and MACD help traders identify trends, momentum shifts, and overbought or oversold conditions.
This project explores the interaction between these two domains:
•	Can financial news sentiment influence stock returns?
•	Can technical indicators reveal market behavior patterns?
•	Is there a measurable statistical relationship between sentiment and price movement?
To answer these questions, financial news headlines and stock market datasets were analyzed for five large technology companies
# Project Objectives
The primary objectives of this project were:
•	Analyze financial news headlines using NLP techniques
•	Perform exploratory data analysis on news datasets
•	Compute technical indicators using TA-Lib
•	Measure daily stock returns
•	Correlate financial news sentiment with stock movement
•	Visualize market behavior using statistical and financial charts
•	Develop a reusable and modular financial analysis pipeline
# Dataset Description
Two major datasets were used throughout the project.
1. Financial News Dataset
Dataset:
•	raw_analyst_ratings.csv
The dataset contains:
•	News headlines
•	Publication dates
•	Publishers
•	Stock ticker symbols
This dataset was used for:
•	Sentiment analysis
•	Topic analysis
•	Publisher analysis
•	Correlation analysis
2. Stock Price Datasets
Separate historical stock datasets were used for:
•	AAPL
•	AMZN
•	GOOG
•	META
•	NVDA
Each stock dataset included:
•	Date
•	Open price
•	High price
•	Low price
•	Close price
•	Volume
These datasets were used for:
•	Technical indicator computation
•	Daily return calculation
•	Trend analysis
•	Correlation analysis
# Methodology
# Task 1 — Exploratory Data Analysis (EDA)
Environment Setup
The project was developed using:
•	Python
•	Jupyter Notebook
•	Git and GitHub
•	GitHub Actions for CI/CD
The repository was organized using a modular project structure with separate directories for:
•	notebooks
•	src
•	tests
•	scripts
•	data
Version control was managed using Git branches and descriptive commit messages following Conventional Commits.
Descriptive Statistics
Several descriptive statistics were computed on the financial news dataset.
Headline Length Analysis
Headline text lengths were analyzed to understand the distribution of article sizes.
Findings:
•	Most headlines were relatively short and concise
•	Extreme headline lengths were rare
•	News providers favored compact financial summaries
Visualization:
•	Histogram of headline character counts
Publisher Analysis
The number of articles published by each publisher was analyzed.
Findings:
•	A small number of publishers dominated financial news coverage
•	Some publishers specialized heavily in technology stocks
•	Publisher contribution was highly imbalanced
Visualization:
•	Bar chart of top publishers
Time-Series News Volume Analysis
Publication dates were analyzed over time.
Findings:
•	Significant spikes in news volume appeared around major market events
•	Earnings periods generated unusually high article activity
•	News publication frequency varied across companies
Visualization:
•	Time-series plot of daily news volume
Topic Modeling and Keyword Analysis
Natural Language Processing techniques were applied using:
•	TF-IDF
•	CountVectorizer
Common recurring financial themes included:
•	earnings beat
•	price target
•	FDA approval
•	market volatility
•	revenue growth
Findings:
•	Financial headlines frequently emphasized earnings and analyst expectations
•	Sentiment-heavy words were commonly associated with strong market reactions
# Task 2 — Quantitative Analysis Using TA-Lib
# Data Preparation
Historical stock datasets were cleaned using reusable Python functions.
The preprocessing pipeline included:
•	Date conversion
•	Missing value handling
•	Duplicate removal
•	Numeric type validation
•	Sorting by date
Reusable functions improved code maintainability and scalability.
Technical Indicators
Technical indicators were computed using TA-Lib.
The following indicators were analyzed:
Simple Moving Average (SMA)
SMA was used to identify long-term price trends.
Findings:
•	SMA smoothed short-term volatility
•	Trend direction became easier to identify
•	Crossovers often indicated potential trend changes
Exponential Moving Average (EMA)
EMA gives more weight to recent prices.
Findings:
•	EMA reacted faster to price changes than SMA
•	Useful for identifying short-term momentum
•	Provided earlier signals during volatile periods
Relative Strength Index (RSI)
RSI was used to identify overbought and oversold conditions.
Interpretation:
•	RSI above 70 → overbought
•	RSI below 30 → oversold
Findings:
•	Several stocks entered overbought conditions during strong bullish trends
•	Oversold conditions often preceded price recovery periods
MACD (Moving Average Convergence Divergence)
MACD was used to detect momentum shifts and trend reversals.
Findings:
•	MACD crossovers aligned with major momentum changes
•	Histogram behavior helped identify trend strength
•	Technology stocks showed strong momentum during high-volatility periods
# Technical Indicator Visualizations
Three-panel visualizations were created for each company:
1.	Price with SMA and EMA
2.	RSI chart
3.	MACD chart
These visualizations helped explain:
•	Trend direction
•	Momentum shifts
•	Market volatility
•	Reversal patterns
# Task 3 — Correlation Between News Sentiment and Stock Movement
Sentiment Analysis Methodology
Tool Selection
The VADER sentiment analyzer from NLTK was selected.
Reasons for selection:
•	Lightweight and fast
•	Effective for short financial headlines
•	Produces normalized sentiment scores
•	Widely used for sentiment polarity analysis
Each headline received a compound sentiment score ranging from:
•	-1 → highly negative
•	0 → neutral
•	+1 → highly positive

Date Alignment
One of the major challenges involved aligning financial news dates with stock trading dates.
Challenges included:
•	Weekend publications
•	Timezone inconsistencies
•	Mixed datetime formats
Solutions implemented:
•	Datetime normalization
•	Timezone removal
•	Weekend adjustment to next business day
This ensured accurate matching between:
•	Daily sentiment scores
•	Daily stock returns
Daily Return Calculation
Daily stock returns were calculated using:
Daily Return = ((Close_t - Close_t-1) / Close_t-1) × 100
This measured the percentage price movement between consecutive trading days.
Sentiment Aggregation
When multiple articles existed for the same company on the same day:
•	sentiment scores were averaged
•	a single daily sentiment score was generated
This reduced noise and improved statistical consistency.
Correlation Analysis
Pearson correlation coefficients were computed between:
•	average daily sentiment
•	daily stock returns
Scatter plots were used to visualize the relationship.
Results and Findings
Apple (AAPL)
Apple showed a weak positive correlation between sentiment and daily returns.
Example finding:
•	Correlation ≈ 0.10
Interpretation:
•	Positive sentiment occasionally aligned with positive stock returns
•	However, the relationship was relatively weak
•	News sentiment alone was not a strong predictor of short-term price movement
Visualization:
•	Scatter plot of sentiment vs daily returns
•	Bar chart of average returns by sentiment category
Amazon (AMZN)
Amazon demonstrated moderate market volatility and varying sentiment behavior.
Findings:
•	Positive news often coincided with upward momentum
•	Correlation remained relatively weak overall
•	Technical indicators provided clearer trend signals than sentiment alone
Google (GOOG)
Google exhibited relatively stable sentiment behavior.
Findings:
•	Sentiment fluctuations were smaller compared to other stocks
•	Daily returns showed limited sensitivity to headline polarity
Meta (META/FB)
A significant challenge involved ticker normalization.
The news dataset used:
•	FB
while stock datasets used:
•	META
A ticker mapping layer was implemented to correctly align historical data.
This demonstrated a real-world financial data engineering issue.
NVIDIA (NVDA)
NVIDIA showed strong volatility behavior.
Findings:
•	Technical indicators captured momentum changes effectively
•	News sentiment appeared more reactive during periods of rapid market movement
# Investment Strategy Recommendations
Based on the analysis, several investment insights were identified.
1. Combine Technical Analysis with Sentiment Analysis
Sentiment alone is insufficient for reliable prediction.
A stronger approach combines:
•	sentiment indicators
•	technical indicators
•	market trend analysis
2. Use RSI and MACD for Timing Decisions
RSI and MACD provided stronger signals than sentiment alone.
Potential strategy:
•	Buy during oversold RSI conditions with improving sentiment
•	Sell during overbought RSI conditions with weakening momentum
3. Monitor High-Impact News Events
News volume spikes often aligned with:
•	earnings announcements
•	analyst upgrades
•	major company events
These periods may create short-term trading opportunities.
4. Apply Risk Management
Financial news sentiment is noisy and uncertain.
Investors should:
•	diversify portfolios
•	use stop-loss strategies
•	avoid relying solely on sentiment-based trading
# Limitations of the Study
Several limitations affected the analysis.
1. Weak Correlation Strength
Most correlations were weak.
This suggests that:
•	stock prices depend on many external variables
•	sentiment alone cannot fully explain market movement
2. Lag Effects
Markets may react to news after delays.
The analysis only considered same-day relationships.
Future work could analyze:
•	1-day lag
•	multi-day lag effects
3. Limited Sentiment Context
VADER works well for short text but cannot fully understand:
•	sarcasm
•	financial nuance
•	complex analyst language
More advanced transformer-based models may improve accuracy.
4. Market Confounding Factors
Stock prices are influenced by:
•	macroeconomic conditions
•	interest rates
•	geopolitical events
•	institutional trading
These variables were not included.
# Future Improvements
Potential next steps include:
•	Using FinBERT or transformer-based financial NLP models
•	Building predictive machine learning models
•	Adding lagged sentiment analysis
•	Incorporating macroeconomic indicators
•	Creating automated trading signals
•	Deploying dashboards for real-time analysis
# Conclusion
This project successfully integrated:
•	Natural Language Processing
•	Financial technical analysis
•	Statistical correlation analysis
•	Time-series data engineering
The analysis demonstrated that financial news sentiment has some relationship with stock movement, although the relationship is generally weak and inconsistent.
Technical indicators such as RSI and MACD provided stronger and more interpretable market signals.
Most importantly, the project demonstrated how multiple data science disciplines can be combined into a complete end-to-end financial analytics workflow.
The project also highlighted several real-world engineering challenges including:
•	timezone normalization
•	ticker symbol mapping
•	financial data cleaning
•	notebook reproducibility
Overall, this work provides a strong foundation for future financial NLP and quantitative trading research.
Technologies Used
•	Python
•	Pandas
•	NumPy
•	Matplotlib
•	TA-Lib
•	NLTK VADER
•	Jupyter Notebook
•	Git & GitHub
•	GitHub Actions
References
•	NLTK Documentation
•	TA-Lib Documentation
•	Yahoo Finance Historical Data
•	Financial News Datasets
•	Pearson Correlation Methodology
