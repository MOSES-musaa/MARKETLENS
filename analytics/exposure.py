"""
calculates exposure for any option chain
"""
import pandas as pd
from config.settings import CONTRACT_SIZE, SUPPORTED_GREEKS

def calculate_exposure(df: pd.DataFrame,greek:str, contract_size: int = CONTRACT_SIZE) -> pd.DataFrame:

    """
    Calculates exposure for every strike.
    """
    if greek not in SUPPORTED_GREEKS:
        supported=", ".join(SUPPORTED_GREEKS)

        raise ValueError(
            f"Unsupported greek '{greek}'."
            f" Supported greeks are: {supported}"
        )
    
    # Create a copy so we don't modify the original DataFrame
    result = df.copy()

    # Calculate exposure
    result["exposure"] = (
        result[greek]
        * result["call_oi"]
        * contract_size
    )

    return result
#calculate the largest exposure for a given greek

def largest_exposure(df: pd.DataFrame, greek: str) -> pd.Series:
    """
    Returns the strike with the largest exposure.
    """

    index = df["exposure"].idxmax()

    return df.loc[index]

#calculates the smallest exposure for a given greek
def smallest_exposure(df: pd.DataFrame, greek: str) -> pd.Series:
    """
    Returns the strike with the smallest exposure.
    """

    index = df["exposure"].idxmin()

    return df.loc[index]