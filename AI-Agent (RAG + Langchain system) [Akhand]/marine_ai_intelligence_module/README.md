# Marine AI Intelligence Module

This module provides an **AI-powered vessel intelligence system** that analyzes maritime operational data and generates a detailed report explaining ship performance, carbon emissions, anomalies, voyage conditions, and root causes.

It acts as an **AI analysis engine** for the marine smart automation system.

---

# Features

The system can analyze:

- Carbon emissions
- Fuel consumption
- Engine load
- Ship speed
- Wind speed
- Wave height
- Sea temperature
- Vessel efficiency
- Voyage conditions
- Operational anomalies
- Root cause analysis

It also generates a **complete vessel intelligence report** explaining possible reasons affecting ship performance.

---

# Folder Structure


marine_ai_intelligence_module
│
├── data
│ └── master_maritime_dataset.csv
│
├── models
│ └── carbon_emission_model.pkl
│
├── src
│ ├── __init__.py
│ ├── config.py
│ ├── safe_utils.py
│ ├── train_carbon_model.py
│ ├── carbon_predictor.py
│ ├── semantic_router.py
│ ├── query_engine.py
│ ├── anomaly_detector.py
│ ├── voyage_analyzer.py
│ ├── root_cause_analyzer.py
│ ├── explanation_engine.py
│ └── intelligence_layer.py
│
├── requirements.txt
└── README.md


---

# Installation

Install required dependencies:

```bash
pip install -r requirements.txt
Train Carbon Emission Model

Before running the system, train the carbon emission model.

Run:

python -m src.train_carbon_model

This will generate:

models/carbon_emission_model.pkl
Running the AI Intelligence Module

Example usage:

from src.intelligence_layer import answer_question

result = answer_question("Why are carbon emissions high?")
print(result)
Example Output

Example system response:

{
  "question": "Why are carbon emissions high?",
  
  "analysis": {
    "carbon_emission": 1240.6,
    "fuel_consumption": 56.3,
    "engine_load": 82.1,
    "ship_speed": 15.4,
    "wave_height": 2.2,
    "wind_speed": 17.3,
    "sea_temperature": 19.6,
    "efficiency_rate": 0.84
  },

  "voyage_condition": {
    "sea_state": "Moderate Sea",
    "wind_speed": 17.3
  },

  "anomalies": [
    "High engine load anomaly detected"
  ],

  "root_causes": [
    "High engine load increased fuel consumption",
    "Strong wind increased vessel resistance",
    "High wave height increased propulsion demand"
  ],

  "report": "Ship Intelligence Report\n\nAverage CO2 Emission: 1240 tonnes\nAverage Fuel Consumption: 56 tons/day\nAverage Engine Load: 82%\nAverage Ship Speed: 15 knots\nAverage Wind Speed: 17 knots\nAverage Wave Height: 2.2 meters\n\nPossible Reasons:\nHigh engine load increased fuel consumption\nStrong wind increased vessel resistance\nHigh wave height increased propulsion demand"
}