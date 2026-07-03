"""
delta_exposure.py

calculates dex, the dealer delta exposure for an option chain
"""
import pandas as pd

def calculate_dex(df: pd.DataFrame, contract_size: int = 100) -> pd.DataFrame:
    """
    Calculates Dealer Delta Exposure for every strike.
    """

    # Create a copy so we don't modify the original DataFrame
    result = df.copy()

    # Calculate DEX
    result["dex"] = (
        result["delta"]
        * result["call_oi"]
        * contract_size
    )

    return result

def largest_dex(df: pd.DataFrame) -> pd.Series:
    """
    Returns the row containing the largest Dealer Delta Exposure.
    """

    index = df["dex"].idxmax()

    return df.loc[index]

def smallest_dex(df: pd.DataFrame) -> pd.Series:
    """
    Returns the row containing the smallest Dealer Delta Exposure.
    """

    index = df["dex"].idxmin()

    return df.loc[index]

def print_dex_summary(df: pd.DataFrame) -> None:
    """
    Prints a summary of Dealer Delta Exposure.
    """
    print("\n========== DEALER DELTA EXPOSURE ==========")

    largest = largest_dex(df)
    print(f"Largest DEX Strike: {largest['strike']}")
    print(f"Largest DEX: {largest['dex']:,.0f}")

    print()

    smallest = smallest_dex(df)
    print(f"Smallest DEX Strike: {smallest['strike']}")
    print(f"Smallest DEX: {smallest['dex']:,.0f}")

    