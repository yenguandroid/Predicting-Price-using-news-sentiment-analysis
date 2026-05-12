# Predicting-Price-using-news-sentiment-analysis
This project focuses on two important analytical areas:

Exploratory analysis of financial news data Quantitative analysis of stock market price data using technical indicators

The project combines financial news analysis with quantitative technical analysis to better understand relationships between news activity, market sentiment, and stock price behavior. 2. Objectives

The main objectives of this project are:

Task 1 Objectives Perform exploratory data analysis (EDA) on financial news headlines Analyze headline characteristics and publication behavior Identify temporal publication patterns Understand news distribution trends over time Prepare cleaned and structured datasets for future sentiment analysis Task 2 Objectives Load and clean historical stock market datasets Compute technical indicators using TA-Lib Analyze stock market behavior using quantitative methods Visualize stock trends and technical indicators Compare market behavior across multiple technology companies Build reusable and modular financial data analysis functions
# Task 1: Exploratory Data Analysis of Financial News
# Data Preparation and Cleaning

The financial news dataset was initially loaded into a pandas DataFrame for preprocessing and exploratory analysis.

The following preprocessing steps were performed:
# 1. dataset loading, missing value inspection & datetime conversion 

# load data
import pandas as pd

df = pd.read_csv("../data/raw/raw_analyst_ratings.csv")
df.head()         
# 2. headline length computation #Descriptive Statistics #Headline Length
# Calculate headline length
df['headline_length'] = df['headline'].apply(len)

# Display descriptive statistics
headline_stats = df['headline_length'].describe()

print(headline_stats)

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

plt.hist(df['headline_length'], bins=50)

plt.title("Headline Length Distribution")
plt.xlabel("Headline Length")
plt.ylabel("Frequency")

plt.show()