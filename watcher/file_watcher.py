import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

#Import my cleaning and loading functions
from analytics.data_loader import load_raw_data
from analytics.data_cleaning import clean_data

RAW_PATH = "data/raw_data/Walmart_Sales.csv"
PROCESSED_PATH = "data/processed_data/Walmart_Sales_Cleaned.csv"

class CSVHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith("Walmart_Sales.csv"):
            print(f"Change detected in {event.src_path}. Processing data ...")

            df_raw = load_raw_data(RAW_PATH)

            df_clean = clean_data(df_raw)

            df_clean.to_csv(PROCESSED_PATH, index=False)
            print(f"Processed data saved to {PROCESSED_PATH}\n")

if __name__ == "__main__":
    event_handler = CSVHandler()
    observer = Observer()

    folder_to_watch = os.path.dirname(RAW_PATH)
    observer.schedule(event_handler, path=folder_to_watch, recursive=False)

    print(f"Watching for changes in {folder_to_watch}...")
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()