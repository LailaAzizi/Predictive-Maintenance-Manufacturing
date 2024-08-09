import pandas as pd
import sqlite3

def load_data(database_path):
    conn = sqlite3.connect(database_path)
    query = "SELECT * FROM sensor_data;"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def preprocess_data(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.set_index('timestamp', inplace=True)
    return df
