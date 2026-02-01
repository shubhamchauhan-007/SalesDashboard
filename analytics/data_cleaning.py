def clean_data(df):

    df = df.copy()

    df = df.dropna()
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month

    return df