from .query_engine import process_question
from .explanation_engine import generate_explanation
from .anomaly_detector import detect_anomalies
from .voyage_analyzer import analyze_voyage
from .root_cause_analyzer import analyze_root_cause

def answer_question(question):

    try:

        data = process_question(question)

        explanation = generate_explanation(question,data)

        anomalies = detect_anomalies()

        voyage = analyze_voyage()

        causes = analyze_root_cause()

        return {

        "question": question,

        "analysis": data,

        "voyage_condition": voyage,

        "anomalies": anomalies,

        "root_causes": causes,

        "report": explanation

        }

    except Exception:

        return {

        "question": question,

        "error": "System could not process request"

        }