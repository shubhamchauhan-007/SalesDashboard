import matplotlib.pyplot as plt

def sales_trend(df):
    trend = df.groupby('Date')['Weekly_Sales'].sum()
    plt.figure(figsize=(12,5))
    plt.plot(trend.index, trend.value)
    plt.title("Overall Sales Trend")
    plt.xlabel("Date")
    plt.ylabel("Weekly Sales")
    plt.show()