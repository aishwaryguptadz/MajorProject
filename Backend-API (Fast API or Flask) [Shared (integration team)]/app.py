from database import get_connection
import os
import sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add ml_model/src to Python path
current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, ".."))

ml_src = os.path.join(project_root, "ml_model", "src")
sys.path.append(ml_src)

from predict import MaritimePredictor

predictor = MaritimePredictor()


@app.post("/route")
def get_routes(origin: str, destination: str, ship_type: str = None):

    routes = predictor.recommend_routes(
        origin=origin,
        destination=destination,
        ship_type=ship_type,
        top_k=3
    )

    return {"routes": routes}


@app.get("/ports")
def get_ports():
    ports = predictor.get_ports()
    return ports

@app.get("/vessel/metrics")
def get_vessel_metrics():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT TOP 10 engineTemp, rpm, fuelRate, speed,
               vibration, loadWeight, timestamp
        FROM vessel_metrics
        ORDER BY timestamp DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    result = []
    for r in rows:
        result.append({
            "engineTemp": r.engineTemp,
            "rpm": r.rpm,
            "fuelRate": r.fuelRate,
            "speed": r.speed,
            "vibration": r.vibration,
            "loadWeight": r.loadWeight,
            "timestamp": r.timestamp
        })

    return result

@app.get("/prediction/fuel")
def fuel_prediction():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT TOP 1 currentRPM, recommendedRPM,
               estimatedSaving, confidence
        FROM fuel_predictions
        ORDER BY created_at DESC
    """)

    r = cursor.fetchone()
    conn.close()
    if r is None:
        return {"message": "No fuel prediction found"}

    return {
        "currentRPM": r.currentRPM,
        "recommendedRPM": r.currentRPM + r.recommendedRPM,
        "estimatedSaving": r.estimatedSaving,
        "confidence": r.confidence
    }

@app.get("/prediction/safety")
def safety_prediction():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT TOP 1 riskScore, riskLevel, possibleCause
        FROM safety_predictions
        ORDER BY created_at DESC
    """)

    r = cursor.fetchone()
    conn.close()
    if r is None:
        return {"message": ""}

    return {
        "riskScore": r.riskScore,
        "riskLevel": r.riskLevel,
        "possibleCause": r.possibleCause
    }

@app.get("/alerts")
def get_alerts():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT alert_id, severity, message, time
        FROM alerts
        ORDER BY time DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    alerts = []
    for r in rows:
        alerts.append({
            "alertId": r.alert_id,
            "severity": r.severity,
            "message": r.message,
            "time": r.time
        })

    return alerts

@app.get("/logs")
def get_logs():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT event, level, time
        FROM system_logs
        ORDER BY time DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    logs = []
    
    for r in rows:
        logs.append({
            "event": r.event,
            "level": r.level,
            "time": r.time
        })

    return logs

@app.get("/vessel/status")
def vessel_status():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT systemHealth, connectivity
        FROM system_status
    """)

    r = cursor.fetchone()
    conn.close()
    if r is None:
        return {"message": "No fuel prediction found"}

    return {
        "systemHealth": r.systemHealth,
        "connectivity": r.connectivity
    }

from pydantic import BaseModel

class SettingsUpdate(BaseModel):
    refreshInterval: int
    aiMode: str
    apiEndpoint: str


@app.post("/settings/update")
def update_settings(data: SettingsUpdate):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO settings(refreshInterval, aiMode, apiEndpoint)
        VALUES (?, ?, ?)
    """, data.refreshInterval, data.aiMode, data.apiEndpoint)

    conn.commit()
    conn.close()

    return {"message": "Settings updated successfully"}
