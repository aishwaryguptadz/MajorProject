from .query_engine import process_question
from .explanation_engine import generate_explanation

def answer_question(question):

    try:

        data = process_question(question)

        explanation = generate_explanation(question, data)

        return {
            "question": question,
            "analysis": data,
            "explanation": explanation
        }

    except Exception:

        return {
            "question": question,
            "error": "System could not process request"
        }