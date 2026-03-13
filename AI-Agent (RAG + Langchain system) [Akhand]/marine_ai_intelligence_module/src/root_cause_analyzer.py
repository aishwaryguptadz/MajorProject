import pandas as pd
from .config import DATA_PATH
from .safe_utils import safe_mean

df = pd.read_csv(DATA_PATH)

def analyze_root_cause():

    causes = []

    # Safely compute averages
    engine = safe_mean(df, "engine_load_pct")
    wind = safe_mean(df, "wind_speed_knots")
    wave = safe_mean(df, "wave_height_m")
    fuel = safe_mean(df, "fuel_consumption_t_day")
    carbon = safe_mean(df, "co2_emitted_tonnes")
    speed = safe_mean(df, "avg_speed_knots")
    temp = safe_mean(df, "sea_temp_c")

    # Engine related
    if engine is not None and engine > 80:
        causes.append("High engine load increased fuel consumption and emissions")

    # Weather related
    if wind is not None and wind > 15:
        causes.append("Strong wind increased vessel resistance")

    if wave is not None and wave > 2:
        causes.append("High wave height increased propulsion demand")

    # Fuel issues
    if fuel is not None and fuel > 55:
        causes.append("Fuel consumption is higher than normal operating conditions")

    # Emission issue
    if carbon is not None and carbon > 1200:
        causes.append("Carbon emission levels are unusually high")

    # Speed issue
    if speed is not None and speed > 18:
        causes.append("High vessel speed may increase fuel usage")

    # Temperature issue
    if temp is not None and temp > 30:
        causes.append("High sea temperature may affect engine efficiency")

    # If no issues detected
    if len(causes) == 0:
        causes.append("No major operational issues detected")

    return causes