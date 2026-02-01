from analytics.data_loader import load_raw_data
from analytics.data_cleaning import clean_data
from dashboard.dashboard import run_dashboard


RAW_PATH = "data/raw_data/Wallmart_Sales.csv"

df_raw = load_raw_data(RAW_PATH)
df_clean = clean_data(df_raw)

run_dashboard(df_clean)