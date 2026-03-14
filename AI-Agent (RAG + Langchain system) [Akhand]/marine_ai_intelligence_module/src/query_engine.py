import pandas as pd
from .config import DATA_PATH
from .safe_utils import safe_mean
from .router import extract_tags

df = pd.read_csv(DATA_PATH)

def process_question(question):

    tags = extract_tags(question)

    return {

    "tags":tags,

    "carbon_emission":safe_mean(df,"co2_emitted_tonnes"),

    "fuel_consumption":safe_mean(df,"fuel_consumption_t_day"),

    "engine_load":safe_mean(df,"engine_load_pct"),

    "ship_speed":safe_mean(df,"avg_speed_knots"),

    "wave_height":safe_mean(df,"wave_height_m"),

    "wind_speed":safe_mean(df,"wind_speed_knots"),

    "sea_temperature":safe_mean(df,"sea_temp_c")

    }