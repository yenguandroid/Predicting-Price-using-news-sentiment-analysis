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