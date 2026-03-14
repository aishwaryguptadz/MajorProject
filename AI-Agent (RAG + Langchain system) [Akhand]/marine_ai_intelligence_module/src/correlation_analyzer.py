import pandas as pd
from .config import DATA_PATH

df = pd.read_csv(DATA_PATH)

def analyze_correlations():

    corr = df.corr(numeric_only=True)

    results=[]

    if corr["fuel_consumption_t_day"]["engine_load_pct"]>0.5:
        results.append("Fuel consumption strongly correlates with engine load")

    if corr["co2_emitted_tonnes"]["fuel_consumption_t_day"]>0.7:
        results.append("Carbon emissions increase with fuel consumption")

    return results