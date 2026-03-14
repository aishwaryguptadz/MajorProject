def generate_explanation(question,data):

    report=f"""
Ship Intelligence Report

Carbon Emission: {data["carbon_emission"]}

Fuel Consumption: {data["fuel_consumption"]}

Engine Load: {data["engine_load"]}

Ship Speed: {data["ship_speed"]}

Wind Speed: {data["wind_speed"]}

Wave Height: {data["wave_height"]}

Sea Temperature: {data["sea_temperature"]}

"""

    return report