import pandas as pd
from .config import DATA_PATH

df = pd.read_csv(DATA_PATH)

def detect_anomalies():

    anomalies=[]

    if df["engine_load_pct"].mean()>80:
        anomalies.append("High engine load anomaly")

    if df["fuel_consumption_t_day"].mean()>55:
        anomalies.append("Fuel consumption anomaly")

    if df["wave_height_m"].mean()>2:
        anomalies.append("Rough sea condition")

    if len(anomalies)==0:
        anomalies.append("No anomalies detected")

    return anomalies