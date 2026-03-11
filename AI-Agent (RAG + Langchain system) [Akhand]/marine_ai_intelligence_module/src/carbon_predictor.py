import joblib
import pandas as pd
from config import MODEL_PATH, FEATURES

try:
    model = joblib.load(MODEL_PATH)
except:
    model = None


def predict_emission(data):

    if model is None:
        return None

    try:

        df = pd.DataFrame([data])

        prediction = model.predict(df[FEATURES])[0]

        return prediction

    except:
        return None