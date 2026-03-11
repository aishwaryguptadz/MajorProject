import pandas as pd
from .config import DATA_PATH
from .semantic_router import classify_question
from .safe_utils import safe_mean

df = pd.read_csv(DATA_PATH)

def process_question(question):

    topic=classify_question(question)

    if topic=="carbon":
        return {"metric":"carbon","value":safe_mean(df,"co2_emitted_tonnes")}

    if topic=="fuel":
        return {"metric":"fuel","value":safe_mean(df,"fuel_consumption_t_day")}

    if topic=="engine":
        return {"metric":"engine","value":safe_mean(df,"engine_load_pct")}

    if topic=="speed":
        return {"metric":"speed","value":safe_mean(df,"avg_speed_knots")}

    if topic=="weather":
        return {"metric":"weather","value":safe_mean(df,"wave_height_m")}

    if topic=="efficiency":
        return {"metric":"efficiency","value":safe_mean(df,"is_efficient")}

    return {"metric":"unknown","value":None}