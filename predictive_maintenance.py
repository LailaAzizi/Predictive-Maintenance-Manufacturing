import pandas as pd
from sklearn.ensemble import IsolationForest
from data_preprocessing import load_data, preprocess_data

def detect_anomalies(df):
    # Use Isolation Forest for anomaly detection
    model = IsolationForest(contamination=0.01)
    df['anomaly'] = model.fit_predict(df[['sensor_value']])
    return df

if __name__ == "__main__":
    df = load_data('sensor_data.db')
    df = preprocess_data(df)
    df_with_anomalies = detect_anomalies(df)
    print(df_with_anomalies[df_with_anomalies['anomaly'] == -1])  # Print detected anomalies
