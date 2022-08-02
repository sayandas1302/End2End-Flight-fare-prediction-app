import datetime
import pandas as pd

# finding the column names
def find_col_name():
    column_name=pd.read_csv('data_cleaned.csv').columns
    return column_name

col_names=find_col_name()
source_names=[name.split("_")[1] for name in col_names if 'Sources' in name]
destination_names=[name.split("_")[1] for name in col_names if 'Destinations' in name]
airline_names=[name.split("_")[1] for name in col_names if "Airline" in name]