def call_put_ratio(df):
    """
    Returns the Call/Put Open Interest Ratio.
    """

    total_call = df["call_oi"].sum()
    total_put = df["put_oi"].sum()

    if total_put == 0:
        return None

    return round(total_call / total_put, 2)


def average_call_iv(df):
    """
    Returns the average Call Implied Volatility.
    """

    return round(df["call_iv"].mean(), 2)


def average_put_iv(df):
    """
    Returns the average Put Implied Volatility.
    """

    return round(df["put_iv"].mean(), 2)


def highest_iv_strike(df):
    """
    Returns the strike with the highest implied volatility.
    """

    # Average Call IV and Put IV for each strike
    average_iv = (df["call_iv"] + df["put_iv"]) / 2

    idx = average_iv.idxmax()

    return df.loc[idx]