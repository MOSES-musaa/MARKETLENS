INTERPRETATION_TEMPLATES = {
    "delta": {
        "Very High": (
            "High Dealer Delta Exposure detected at strike {strike}.\n"
            "Dealers may actively hedge around this level.\n"
            "Expect stronger market reactions if price approaches this strike."
        ),
        "High": (
            "Moderate Dealer Delta Exposure at strike {strike}.\n"
            "Dealer hedging pressure is likely to be limited."
        )
    },
    "gamma": {
        "Very High": (
            "High Gamma Exposure detected at strike {strike}.\n"
            "Small price movements may force dealers to hedge aggressively.\n"
            "Expect increased volatility near this level."
        ),
        "High": (
            "Moderate Gamma Exposure at strike {strike}.\n"
            "Dealer hedging activity is expected to be relatively mild."
        )
    }
}

def classify_exposure(exposure: float, max_exposure :float) -> str:
    """
    Classifies the exposure level based on the maximum exposure.

    """

    strength = exposure / max_exposure

    if strength >= 0.80:
        return "Very High"
    elif strength >= 0.60:
        return "High"
    elif strength >= 0.40:
        return "Moderate"
    else:
        return "Low"    


def interpret_exposure(greek: str, strength:str, strike: float) -> str:
    """
    Interprets the largest exposure position.
    """
    template = INTERPRETATION_TEMPLATES[greek][strength]
    if template is None:
        return "No interpretation available for this Greek."
    return template.format(strike=str(strike), strength=strength)