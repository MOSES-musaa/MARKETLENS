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
        ),
        "Moderate":(
            "Moderate Dealer delta Exposure detected at strike {strike}.\n"
             "Dealer hedging activity may have a noticeable influence around this level"
                ),
        "Low":(
            "Low dealer delta Exposure detected at strike {strike}.\n"
            "Limited dealer hedging influence is expected around this level"
                )
    },
    "gamma": {
        "Very High": (
            "Very High Gamma Exposure detected at strike {strike}.\n"
            "Small price movements may force dealers to hedge aggressively.\n"
            "Expect increased volatility near this level."
        ),
        "High": (
            "High Gamma Exposure at strike {strike}.\n"
            "Dealer hedging activity is expected to be relatively mild."
        ),
        "Moderate":(
            "Moderate Gamma Exposure detected at strike {strike}.\n"
            "Dealer hedging activity may have a noticeable influence around this level"
        ),
        "Low":(
            "Low Gamma Exposure detected at strike {strike}.\n"
            "Limited dealer hedging influence is expected around this level"
        )
    }
}

def classify_exposure(exposure: float, max_exposure :float) -> str:
    """
    Classifies the exposure level based on the maximum exposure. """

    if max_exposure == 0:
        raise ValueError(
            "Cannot classify exposure when maximum exposure is zero."
        )

    strength = abs(exposure) / max_exposure

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
    greek_templates = INTERPRETATION_TEMPLATES.get(greek)

    if greek_templates is None:
        raise ValueError(
            f"No Interpretation template available for greek '{greek}'."
        )
    template =greek_templates.get(strength)

    if template is None:
        return "No interpretation available for this exposure strength."

    return template.format(
        strike= str(strike),
        strength=strength
    )
