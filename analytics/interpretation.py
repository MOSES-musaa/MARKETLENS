import pandas as pd


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


def interpret_exposure(position: pd.Series, greek: str) -> str:
    """
    Interprets the largest exposure position.
    """

    strike = position["strike"]
    exposure = position["exposure"]

    if greek == "delta":

        if exposure =="Very High":
            return (
                f"High Dealer Delta Exposure detected at strike {strike}.\n"
                "Dealers may actively hedge around this level.\n"
                "Expect stronger market reactions if price approaches this strike."
            )

        else:
            return (
                f"Moderate Dealer Delta Exposure at strike {strike}.\n"
                "Dealer hedging pressure is likely to be limited."
            )

    elif greek == "gamma":

        if exposure == "Very High":
            return (
                f"High Gamma Exposure detected at strike {strike}.\n"
                "Small price movements may force dealers to hedge aggressively.\n"
                "Expect increased volatility near this level."
            )

        else:
            return (
                f"Moderate Gamma Exposure at strike {strike}.\n"
                "Dealer hedging activity is expected to be relatively mild."
            )

    else:
        return "Unknown exposure type."