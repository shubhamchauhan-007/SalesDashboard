def total_sales(df):
    return df['Weekly_sales'].sum()

def average_weekly_sales(df):
    return df['Weekly_Sales'].mean()

def store_wise_sales(df):
    return df.groupby('Store')['Weekly_Sales'].sum()
