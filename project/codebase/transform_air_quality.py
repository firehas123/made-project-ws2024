import pandas as pd

def preprocess_air_quality(air_quality_df):
    """Preprocess air quality data."""
    print("Preprocessing air quality data...")

    try:
        # Drop rows with missing sample_measurement
        air_quality_df = air_quality_df.dropna(subset=["sample_measurement"])

        # Remove negative sample measurements
        air_quality_df = air_quality_df[air_quality_df["sample_measurement"] >= 0]

        # Convert date_local to datetime
        if "date_local" in air_quality_df.columns:
            air_quality_df["date_local"] = pd.to_datetime(air_quality_df["date_local"], errors="coerce")

        # Replace state_code value 6 with 'CA'
        if "state_code" in air_quality_df.columns:
            air_quality_df["state_code"] = air_quality_df["state_code"].replace(6, "CA")

        # Keep only relevant columns
        relevant_columns = [
            "state_code", "county_code", "site_number", "parameter", "date_local", "sample_measurement", "units_of_measure"
        ]
        air_quality_df = air_quality_df[relevant_columns]
        print("Irrelevant columns removed.")

        # Save the transformed data to a CSV file
        air_quality_file = "transformed_air_quality_data.csv"
        air_quality_df.to_csv(air_quality_file, index=False)
        print(f"Transformed Air Quality data saved to {air_quality_file}")

        return air_quality_df

    except Exception as e:
        print(f"Error during Air Quality Data transformation: {e}")
        return None
