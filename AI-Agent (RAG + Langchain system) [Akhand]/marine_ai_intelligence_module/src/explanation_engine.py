from .safe_utils import safe_value

def generate_explanation(question,data):

    carbon = safe_value(data["carbon_emission"])
    fuel = safe_value(data["fuel_consumption"])
    engine = safe_value(data["engine_load"])
    speed = safe_value(data["ship_speed"])
    wind = safe_value(data["wind_speed"])
    wave = safe_value(data["wave_height"])
    temp = safe_value(data["sea_temperature"])
    efficiency = safe_value(data["efficiency_rate"])

    explanation = f"""
Ship Intelligence Report

Average CO2 Emission: {carbon} tonnes
Average Fuel Consumption: {fuel} tons/day
Average Engine Load: {engine} %
Average Ship Speed: {speed} knots
Average Wind Speed: {wind} knots
Average Wave Height: {wave} meters
Average Sea Temperature: {temp} °C
Efficiency Rate: {efficiency}

Possible Reasons Affecting Ship Performance:
"""

    if engine != "Data not available" and engine > 75:
        explanation += "\n• High engine load increased fuel consumption."

    if wind != "Data not available" and wind > 15:
        explanation += "\n• Strong wind speed increased aerodynamic resistance."

    if wave != "Data not available" and wave > 2:
        explanation += "\n• High wave height increased propulsion resistance."

    explanation += "\n\nThese factors collectively influence vessel efficiency."

    return explanation