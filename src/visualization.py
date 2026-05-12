import matplotlib.pyplot as plt


def plot_technical_indicators(df, company):

    fig, axes = plt.subplots(
        3,
        1,
        figsize=(14, 6),
        sharex=True
    )

    # =========================
    # 1. PRICE + MOVING AVERAGES
    # =========================
    axes[0].plot(df.index, df['Close'], label='Close Price')
    axes[0].plot(df.index, df['SMA_20'], label='SMA 20')
    axes[0].plot(df.index, df['EMA_20'], label='EMA 20')

    axes[0].set_title(f"{company} Price with SMA & EMA", fontsize=16)
    axes[0].set_xlabel("Date", fontsize=12)
    axes[0].set_ylabel("Price (USD)", fontsize=12)
    axes[0].legend()
    axes[0].grid(True, linestyle='--', alpha=0.6)


    # =========================
    # 2. RSI PANEL
    # =========================
    axes[1].plot(df.index, df['RSI'], label='RSI')

    # Overbought & Oversold lines
    axes[1].axhline(70, linestyle='--')
    axes[1].axhline(30, linestyle='--')

    axes[1].set_title(f"{company} RSI")
    axes[1].set_xlabel("Date", fontsize=12)
    axes[1].set_ylabel("RSI", fontsize=12)
    axes[1].legend()
    axes[1].grid(True)

    # =========================
    # 3. MACD PANEL
    # =========================
    axes[2].plot(df.index, df['MACD'], label='MACD')
    axes[2].plot(df.index, df['MACD_SIGNAL'], label='Signal Line')

    axes[2].bar(
        df.index,
        df['MACD_HIST'],
        label='Histogram'
    )

    axes[2].set_title(f"{company} MACD")
    axes[2].set_xlabel("Date", fontsize=12)
    axes[2].set_ylabel("MACD", fontsize=12)
    axes[2].legend()
    axes[2].grid(True)

    plt.tight_layout()

    plt.show()