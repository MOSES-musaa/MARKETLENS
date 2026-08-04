"""Processing utilities for preparing the option chain data before analytics"""

def sort_by_strike(df):
    """
    sorts the option chain by strike price in ascending order
    """
    return df.sort_values(by="strike", ascending=True)

def reset_data_frame_index(df):
    """
    resets the index of the dataframe
    """
    return df.reset_index(drop=True)

def process_option_chain(df):
    """
    Applies all the processing steps to the option chain dataframe
    """
    df = sort_by_strike(df)
    df = reset_data_frame_index(df)
    return df