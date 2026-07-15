"""
calculates exposure for any option chain
"""
import pandas as pd

def calculate_exposure(df: pd.DataFrame,greek:str, contract_size: int = 100) -> pd.DataFrame:

    """
    Calculates exposure for every strike.
    """
    
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