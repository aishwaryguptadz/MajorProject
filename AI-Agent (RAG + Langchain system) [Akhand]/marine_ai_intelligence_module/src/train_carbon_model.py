import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib
from config import DATA_PATH, FEATURES, TARGET, MODEL_PATH

df = pd.read_csv(DATA_PATH)

df = df.dropna(subset=FEATURES + [TARGET])

X = df[FEATURES]
y = df[TARGET]

X_train, X_test, y_train, y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
)

model = RandomForestRegressor()

model.fit(X_train,y_train)

joblib.dump(model,MODEL_PATH)

print("Carbon emission model trained and saved.")