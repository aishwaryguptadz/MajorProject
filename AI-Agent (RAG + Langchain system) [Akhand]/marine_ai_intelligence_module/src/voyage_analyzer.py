import pandas as pd
from .config import DATA_PATH

df = pd.read_csv(DATA_PATH)

def analyze_voyage():

    wind = df["wind_speed_knots"].mean()
    wave = df["wave_height_m"].mean()

    if wave > 2:
        sea_state = "Rough Sea"
    elif wave > 1:
        sea_state = "Moderate Sea"
    else:
        sea_state = "Calm Sea"

    return {
        "sea_state": sea_state,
        "wind_speed": wind
    }