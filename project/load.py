import pandas as pd


def load_data():
    """Load the air quality and respiratory data."""
    print("Loading data...")
    air_quality_file = "air_quality_data.csv"
    respiratory_file = "respiratory_data.csv"

    try:
        air_quality_df = pd.read_csv(air_quality_file)
        respiratory_df = pd.read_csv(respiratory_file)
        print("Data successfully loaded.")
        return air_quality_df, respiratory_df
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None, None


def merge_data(air_quality_df, respiratory_df):
    """Merge the air quality and respiratory data."""
    print("Merging data...")
    
    # Check if the input DataFrames are not None
    if air_quality_df is None:
        raise ValueError("Air Quality DataFrame is None. Ensure data transformation was successful.")
    if respiratory_df is None:
        raise ValueError("Respiratory DataFrame is None. Ensure data transformation was successful.")
    
    # Ensure `state_code` exists in both DataFrames
    if "state_code" not in air_quality_df.columns:
        raise ValueError("Column 'state_code' is missing in Air Quality DataFrame.")
    if "state_code" not in respiratory_df.columns:
        raise ValueError("Column 'state_code' is missing in Respiratory DataFrame.")

    # Ensure `state_code` in both DataFrames is of the same type (convert to string for consistency)
    air_quality_df["state_code"] = air_quality_df["state_code"].astype(str)
    respiratory_df["state_code"] = respiratory_df["state_code"].astype(str)

    # Merge the DataFrames
    merged_df = pd.merge(
        air_quality_df,
        respiratory_df,
        how="inner",
        on="state_code"  # Ensure this key exists in both DataFrames
    )
    print(f"Merged data contains {len(merged_df)} rows.")
    return merged_df


def save_data(df, file_name):
    """Save DataFrame to a CSV file."""
    if df is None or df.empty:
        raise ValueError("Cannot save an empty or None DataFrame.")
    print(f"Saving data to {file_name}...")
    df.to_csv(file_name, index=False)
    print(f"Data saved to {file_name}.")




