import pandas as pd


def read_csv_file(csv_file: str):
    try:
        csv_file = pd.read_csv(csv_file)
        return csv_file
    except Exception as e:
        print(f"Error while reading csv file: {e}")
        return []
