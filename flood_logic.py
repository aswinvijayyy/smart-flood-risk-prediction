def calculate_flood_risk(rainfall_mm, drainage):
    """
    rainfall_mm : mm/hour (from API)
    drainage : 'Good', 'Average', 'Poor'
    """

    # Drainage impact factors
    drainage_factor = {
        "Good": 0.7,
        "Average": 1.0,
        "Poor": 1.5
    }

    # Base risk score
    risk_score = rainfall_mm * drainage_factor[drainage]

    # Risk classification
    if risk_score < 10:
        level = "LOW"
    elif risk_score < 30:
        level = "MODERATE"
    else:
        level = "HIGH"

    return risk_score, level
