def validate_dataframe(df):
    """
    Prints basic information about a DataFrame.
    """

    print("\n========== DATA VALIDATION ==========")

    print(f"\nRows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    print("\nColumn Names:")

    for column in df.columns:
        print(f"  • {column}")

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nSummary Statistics:")
    print(df.describe())

    print("\n====================================")