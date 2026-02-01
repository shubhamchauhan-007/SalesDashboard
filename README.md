# Sales Data Analytics Dashboard

#Project Description:
A Python-based dashboard to analyze Walmart sales data. 
The project automatically cleans, processes, and visualizes sales data, 
and supports real-time monitoring of new data using a watchdog.


#Features
## Features
- Load and clean raw sales data (handle missing values, add Year & Month columns)
- Automatic detection of new CSV files using Watchdog
- Dashboard visualizations for sales trends, KPIs, and more
- Processed data saved in `processed_data` folder
- Handles missed data if system was offline (scheduled/scripted run)


#Folder Structure
## Folder Structure

sales_dashboard/
│
├── data/
│   ├── raw_data/                # Original CSV files
│   └── processed_data/          # Cleaned and processed data
│
├── analytics/
│   ├── data_loader.py           # Load raw CSV files
│   ├── data_cleaning.py         # Clean and enrich data
│   └── metrics.py               # KPI calculations (optional)
│
├── dashboard/
│   ├── visualizations.py        # Functions to create graphs
│   └── dashboard.py             # Run dashboard visualizations
│
├── watcher/
│   └── file_watcher.py          # Watchdog automation for new data
│
├── main.py                      # Main script to run the project
└── requirements.txt             # Required Python packages

