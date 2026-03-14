from .query_engine import process_question
from .anomaly_detector import detect_anomalies
from .voyage_analyzer import analyze_voyage
from .root_cause_analyzer import analyze_root_cause
from .correlation_analyzer import analyze_correlations
from .explanation_engine import generate_explanation
from .memory_manager import save_message

def answer_question(question):

    data = process_question(question)

    tags = data["tags"]

    anomalies = detect_anomalies()

    voyage = analyze_voyage()

    causes = analyze_root_cause(tags)

    correlations = analyze_correlations()

    report = generate_explanation(question,data)

    response = {

    "question":question,

    "detected_topics":tags,

    "analysis":data,

    "voyage_condition":voyage,

    "anomalies":anomalies,

    "root_causes":causes,

    "correlations":correlations,

    "report":report

    }

    save_message(question,response)

    return response