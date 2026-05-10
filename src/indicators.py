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