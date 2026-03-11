from .safe_utils import safe_value

def generate_explanation(question,data):

    metric=data["metric"]
    value=safe_value(data["value"])

    explanations={
    "carbon":f"Average CO2 emission is {value} tonnes caused mainly by fuel usage and engine load.",
    "fuel":f"Average fuel consumption is {value} tons per day.",
    "engine":f"Engine load averages {value}%.",
    "speed":f"Ship speed averages {value} knots.",
    "weather":f"Wave height averages {value} meters affecting propulsion resistance.",
    "efficiency":f"{safe_value(data['value']*100)}% of operations are efficient."
    }

    return explanations.get(metric,"The system could not interpret the question.")