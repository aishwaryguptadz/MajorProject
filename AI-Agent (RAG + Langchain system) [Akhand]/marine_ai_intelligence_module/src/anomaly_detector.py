import pandas as pd
from .config import DATA_PATH

df = pd.read_csv(DATA_PATH)

def detect_anomalies():

    anomalies = []

    avg_engine = df["engine_load_pct"].mean()
    avg_wave = df["wave_height_m"].mean()
    avg_fuel = df["fuel_consumption_t_day"].mean()

    if avg_engine > 80:
        anomalies.append("High engine load anomaly detected")

    if avg_wave > 2:
        anomalies.append("Rough sea condition anomaly")

    if avg_fuel > 55:
        anomalies.append("Fuel consumption anomaly")

    return anomalies