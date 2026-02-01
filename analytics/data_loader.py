import pandas as pd

def load_raw_data(path):
    df = pd.read_csv(path)
    df['Date'] = pd.to_datetime(df['Date'], format="%d-%m-%Y")
    return df