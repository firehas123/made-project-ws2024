def preprocess_respiratory_data(respiratory_df):
    """Preprocess respiratory data."""
    print("Preprocessing respiratory data...")
    
    # Drop rows with missing essential columns
    respiratory_df = respiratory_df.dropna(subset=["topic", "datavalue"])
    
    # Rename columns for consistency and clarity
    column_renaming = {
        "yearstart": "year",
        "datavalue": "respiratory_value",
        "datavaluetype": "respiratory_value_type",
        "locationabbr": "state_code",
        "locationdesc": "county_name",
    }
    respiratory_df = respiratory_df.rename(columns=column_renaming)
    
    # Convert 'year' column to integer
    if "year" in respiratory_df.columns:
        respiratory_df.loc[:, "year"] = respiratory_df["year"].astype(int, errors="ignore")
    
    # Keep only relevant columns
    relevant_columns = [
        "year", "state_code", "county_name", "topic", "respiratory_value", 
        "respiratory_value_type", "stratificationcategory1", "stratification1"
    ]
    
    # Verify that all relevant columns exist in the DataFrame
    available_columns = respiratory_df.columns.intersection(relevant_columns)
    if set(relevant_columns).issubset(respiratory_df.columns):
        respiratory_df = respiratory_df[relevant_columns]
    else:
        missing_columns = set(relevant_columns) - set(available_columns)
        raise ValueError(f"The following required columns are missing in the dataset: {missing_columns}")
    
    print("Irrelevant columns removed.")
    
    # Save the transformed data to a CSV file
    respiratory_file = "transformed_respiratory_data.csv"
    respiratory_df.to_csv(respiratory_file, index=False)
    print(f"Transformed Respiratory data saved to {respiratory_file}")
    
    return respiratory_df


def filter_relevant_topics(respiratory_df):
    """Filter respiratory data for relevant topics."""
    print("Filtering relevant topics in the respiratory data...")

    relevant_topics = [
        "Asthma",
        "Chronic Obstructive Pulmonary Disease",
        "Cardiovascular Disease",
        "Mental Health",
        "Sleep",
        "Health Status",
    ]

    # Ensure the 'topic' column exists in the DataFrame
    if "topic" not in respiratory_df.columns:
        raise ValueError("The 'topic' column is missing in the respiratory dataset.")

    # Filter rows where the 'topic' column matches the relevant topics
    respiratory_df = respiratory_df[respiratory_df["topic"].isin(relevant_topics)]

    print(f"Filtered data contains {len(respiratory_df)} rows.")
    return respiratory_df