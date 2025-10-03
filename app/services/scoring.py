from flask import current_app

def calculate_sustainability_score(data):
    default_weights = current_app.config.get("WEIGHTS", {
        "gwp": 0.4,
        "circularity": 0.4,
        "cost": 0.2,
    })

    weights = data.get("weights", default_weights)

    max_gwp = current_app.config.get("MAX_GWP", 23900) #for recruiter: Assumption: normalize gwp using highest gwp of PFTBA
    max_cost = current_app.config.get("MAX_COST", 100000) #assumption: max expected cost known: for normalization

    gwp = float(data["gwp"])/max_gwp
    circularity = float(data["circularity"])/100
    cost = float(data["cost"])/max_cost

    score = 100 * ((1 - gwp) * weights["gwp"] + circularity * weights["circularity"] + (1 - cost) * weights["cost"])

    if score >= 95: rating = "A"
    elif score >= 90: rating = "B"
    elif score >= 87: rating = "C"
    else: rating = "D"

    return score, rating