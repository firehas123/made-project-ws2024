from extract import run_data_fetching
from transform import run_transformations
from load import load_data, merge_data, save_data, analyze_data


def main():
    # Step 1: Extract data using threads
    print("---- Extract Phase ----")
    run_data_fetching()

    # Step 2: Load raw data
    print("---- Load Phase ----")
    air_quality_df, respiratory_df = load_data()

    if air_quality_df is not None and respiratory_df is not None:
        try:
            # Step 3: Transform data
            print("---- Transform Phase ----")
            air_quality_df, respiratory_df = run_transformations(air_quality_df, respiratory_df)
            
            # Log the state of the DataFrames
            if air_quality_df is not None:
                print(f"Air Quality DataFrame loaded with {air_quality_df.shape[0]} rows.")
            else:
                print("Air Quality DataFrame is None after transformation.")
            
            if respiratory_df is not None:
                print(f"Respiratory DataFrame loaded with {respiratory_df.shape[0]} rows.")
            else:
                print("Respiratory DataFrame is None after transformation.")
            
            # Step 4: Merge and Save Phase
            print("---- Merge and Save Phase ----")
            if air_quality_df is not None and respiratory_df is not None:
                merged_df = merge_data(air_quality_df, respiratory_df)
                save_data(merged_df, "merged_data.csv")
            else:
                raise ValueError("One or both transformed DataFrames are None. Check the transformation phase.")
        
            print("Pipeline executed successfully.")
        
        except Exception as e:
            print(f"Pipeline execution failed: {e}")
    else:
        print("Pipeline terminated due to missing data.")


if __name__ == "__main__":
    main()
