import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(BASE_DIR, "data", "master_maritime_dataset.csv")
MODEL_PATH = os.path.join(BASE_DIR, "models", "carbon_emission_model.pkl")

FEATURES = [
    "fuel_consumption_t_day",
    "engine_load_pct",
    "shaft_power_kw",
    "avg_speed_knots",
    "wave_height_m",
    "wind_speed_knots",
    "distance_nm"
]

TARGET = "co2_emitted_tonnes"