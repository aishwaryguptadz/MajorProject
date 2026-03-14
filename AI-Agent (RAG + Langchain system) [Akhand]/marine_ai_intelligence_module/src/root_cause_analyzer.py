import pandas as pd
from .config import DATA_PATH

df = pd.read_csv(DATA_PATH)

def analyze_root_cause(tags):

    causes=[]

    if "fuel" in tags and df["engine_load_pct"].mean()>80:
        causes.append("High engine load increased fuel usage")

    if "weather" in tags and df["wave_height_m"].mean()>2:
        causes.append("Rough sea increased propulsion demand")

    if "carbon" in tags and df["fuel_consumption_t_day"].mean()>55:
        causes.append("High fuel usage increased carbon emissions")

    if len(causes)==0:
        causes.append("No major operational issue")

    return causes