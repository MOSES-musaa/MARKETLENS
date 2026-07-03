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