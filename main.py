from analytics.data_loader import load_raw_data
from analytics.data_cleaning import clean_data
from dashboard.dashboard import run_dashboard
import os


RAW_PATH = "data/raw_data/Walmart_Sales.csv"
PROCESSED_PATH = "data/processed_data/walmart_sales_cleaned.csv"

df_raw = load_raw_data(RAW_PATH)
df_clean = clean_data(df_raw)

# Save cleaned data to processed_data folder
os.makedirs(os.path.dirname(PROCESSED_PATH), exist_ok=True)
df_clean.to_csv(PROCESSED_PATH, index=False)
print(f"Processed data saved to {PROCESSED_PATH}")
print(f"Number of cleaned rows: {len(df_clean)}")

run_dashboard(df_clean)