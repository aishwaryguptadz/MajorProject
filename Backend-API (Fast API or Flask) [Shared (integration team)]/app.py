from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import os
import sys
current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, ".."))

ml_src = os.path.join(project_root, "ml_model", "src") 
sys.path.append(ml_src)

from predict import MaritimePredictor
from feature_engineering import create_derived_features

def prepare_features(input_dict):
    import pandas as pd

    df = pd.DataFrame([input_dict])

    # Add derived features
    df = create_derived_features(df)

    # 🔥 Ensure ALL required columns exist
    for col in predictor.fuel_features:
        if col not in df.columns:
            df[col] = 0   # default value

    return df

app = FastAPI()

# ---------------- CORS ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- PATH SETUP ----------------
current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, ".."))

ml_src = os.path.join(project_root, "ml_model", "src")
sys.path.append(ml_src)

from predict import MaritimePredictor

predictor = MaritimePredictor()

# =========================================================
# 🚢 1. ROUTE API
# =========================================================

class RouteRequest(BaseModel):
    origin: str
    destination: str
    ship_type: str = None


@app.post("/route")
def get_routes(data: RouteRequest):
    routes = predictor.recommend_routes(
        origin=data.origin,
        destination=data.destination,
        ship_type=data.ship_type,
        top_k=3
    )
    return {"routes": routes}


# =========================================================
# ❤️ 2. HEALTH API (ML DIRECT)
# =========================================================

class HealthInput(BaseModel):
    rpm: float
    engineTemp: float
    vibration: float
    loadWeight: float


@app.post("/prediction/health")
def get_health(data: HealthInput):

     try:
        # 1. Convert to DataFrame
        df = prepare_features({
        "rpm": data.rpm,
        "engineTemp": data.engineTemp,
        "vibration": data.vibration,
        "loadWeight": data.loadWeight,
        "design_speed_knots": 15,
        "wind_speed": 10,
        "wave_height": 1.5,
        "sea_state": 3
        })
        # 2. Predict using existing model
        prediction = predictor.predict_fuel(df)

        health_score = float(prediction[0])

        # 3. Alert logic
        if health_score >= 80:
            alert = "HEALTHY"
        elif health_score >= 50:
            alert = "WARNING"
        else:
            alert = "CRITICAL"

        return {
            "health_score": health_score,
            "alert_level": alert
        }

     except Exception as e:
        return {"error": str(e)}
        
# =========================================================
# 🚀 3. ROUTE → HEALTH (MAIN FLOW)
# =========================================================

class RouteSelection(BaseModel):
    origin: str
    destination: str
    ship_type: str = None
    route_index: int = 0


@app.post("/voyage/health")
def voyage_health(data: RouteSelection):

    try:
        routes = predictor.recommend_routes(
            origin=data.origin,
            destination=data.destination,
            ship_type=data.ship_type,
            top_k=3
        )

        selected_route = routes[data.route_index]

        # 1. Build DataFrame
        df = prepare_features({
        "rpm": selected_route.get("rpm", 80),
        "engineTemp": selected_route.get("engine_temp", 75),
        "vibration": selected_route.get("vibration", 5),
        "loadWeight": selected_route.get("load", 1000),
        "design_speed_knots": 15,
        "wind_speed": 10,
        "wave_height": 1.5,
        "sea_state": 3
        })
        # 2. Derived features
        print("EXPECTED:", predictor.fuel_features)
        print("GOT:", df.columns)
        prediction = predictor.predict_fuel(df)

        health_score = float(prediction[0])

        # 4. Alert
        if health_score >= 80:
            alert = "HEALTHY"
        elif health_score >= 50:
            alert = "WARNING"
        else:
            alert = "CRITICAL"

        return {
            "selected_route": selected_route,
            "health_score": health_score,
            "alert_level": alert
        }

    except Exception as e:
        return {"error": str(e)}


# =========================================================
# 🤖 4. CHATBOT (AKHAND)
# =========================================================

ai_path = os.path.join(
    project_root,
    "AI-Agent (RAG + Langchain system) [Akhand]",
    "marine_ai_intelligence_module"
)
sys.path.append(ai_path)

from src.query_engine import analyze_dataset

class Query(BaseModel):
    question: str


@app.post("/ask")
def ask_question(data: Query):

    analysis = analyze_dataset()
    question = data.question.lower()

    root_causes = []

    if "fuel" in question:
        root_causes.append("Fuel consumption depends on engine load and speed")
    if "sea" in question:
        root_causes.append("Rough sea increases propulsion demand")
    if "engine" in question:
        root_causes.append("High engine load increases fuel usage")

    return {
        "question": data.question,
        "analysis": analysis,
        "root_causes": root_causes if root_causes else ["General system behavior"],
        "report": "AI-generated maritime insight"
    }