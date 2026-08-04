""""Utilities for saving processed option chain data to CSV files."""
from pathlib import Path

def save_processed_option_chain(df, file_path):
    """
    Save the processed option chain DataFrame to a CSV file into the disk

    Parameters:
    df (pd.DataFrame): The processed option chain DataFrame.
    file_path (str): The path where the CSV file will be saved.
    """
    # Ensure the directory exists
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)

    # Save the DataFrame to CSV
    df.to_csv(file_path, index=False)