
def validate_dataframe(df):
    """
    validates the given dataframe to ensure it has the expected structure and data types
    """

def validate_not_empty(df):
    """
    ensures that the option chain contains data
    """
    if df.empty:
        raise ValueError("Option chain is empty")
    return df

def validate_required_columns(df, required_columns):
    """
    ensures that the option chain contains the required columns
    """
    missing_columns = [
        column for column in required_columns
          if column not in df.columns]
    if missing_columns:
        raise ValueError(f"Option chain is missing required columns: {', '.join(missing_columns)}")
    return df


def validate_option_chain(df, required_columns):
    """
    runs all the validation checks on the option chain dataframe
    """
    validate_not_empty(df)
    validate_required_columns(df, required_columns)
    return df