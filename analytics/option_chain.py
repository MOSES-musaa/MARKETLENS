#returns total Call Open Interest

def total_call_open_interest(df):
    """
    Returns the total Call Open Interest.
    """
    return df["call_oi"].sum()

#returns total Put Open Interest

def total_put_open_interest(df):
    """
    Returns the total Put Open Interest.
    """
    return df["put_oi"].sum()

#returns the strike with the highest Call Open Interest

def largest_call_wall(df):
    """
    Returns the strike with the highest Call Open Interest.
    """

    idx = df["call_oi"].idxmax()

    return df.loc[idx]

#returns the strike with the highest Put Open Interest

def largest_put_wall(df):

    idx = df["put_oi"].idxmax()

    return df.loc[idx]

#Returns the strike closest to the current price

def atm_strike(df, current_price):

    idx = (df["strike"] - current_price).abs().idxmin()

    return df.loc[idx]