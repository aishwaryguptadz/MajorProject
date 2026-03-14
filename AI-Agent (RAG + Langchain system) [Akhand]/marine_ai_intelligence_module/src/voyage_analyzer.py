import pandas as pd
from .config import DATA_PATH

df = pd.read_csv(DATA_PATH)

def analyze_voyage():

    wave = df["wave_height_m"].mean()

    wind = df["wind_speed_knots"].mean()

    if wave>2:
        sea="Rough Sea"

    elif wave>1:
        sea="Moderate Sea"

    else:
        sea="Calm Sea"

    return {

    "sea_state":sea,

    "wind_speed":wind

    }