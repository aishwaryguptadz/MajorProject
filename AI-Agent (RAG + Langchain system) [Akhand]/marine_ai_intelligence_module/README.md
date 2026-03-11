# Marine AI Intelligence Module

This module is part of the **Smart Automation for Marine Vessel Operations** project.

It provides an AI-powered system that analyzes maritime operational data and answers questions about vessel performance and carbon emissions.

---

## Features

- Carbon Emission Prediction using Machine Learning
- Semantic Question Understanding using Sentence Transformers
- Vessel Performance Analysis
- Natural Language Explanations for Ship Data
- Robust Error Handling

---

## Folder Structure
marine_ai_intelligence_module
│
├── data
│ └── master_maritime_dataset.csv
│
├── models
│ └── carbon_emission_model.pkl
│
├── src
│ ├── config.py
│ ├── safe_utils.py
│ ├── train_carbon_model.py
│ ├── carbon_predictor.py
│ ├── semantic_router.py
│ ├── query_engine.py
│ ├── explanation_engine.py
│ └── intelligence_layer.py
│
├── requirements.txt
└── README.md

---

## Installation

Install required dependencies:
pip install -r requirements.txt


---

## Train Carbon Emission Model

Run:
python src/train_carbon_model.py


This will generate:
models/carbon_emission_model.pkl


---

## Running the AI Intelligence Module

Example usage:

```python
from src.intelligence_layer import answer_question

result = answer_question("Why are carbon emissions high?")
print(result)

Example output:

{
 "question": "Why are carbon emissions high?",
 "analysis": {
   "metric": "carbon",
   "value": 1250.4
 },
 "explanation": "Average CO2 emission is 1250 tonnes caused mainly by fuel usage and engine load."
}

Example output:

{
 "question": "Why are carbon emissions high?",
 "analysis": {
   "metric": "carbon",
   "value": 1250.4
 },
 "explanation": "Average CO2 emission is 1250 tonnes caused mainly by fuel usage and engine load."
}