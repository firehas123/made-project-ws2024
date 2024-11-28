from extract import run_data_fetching
from transform import run_transformations
from load import load_data, merge_data, save_data


def main():
    # Step 1: Extract data using threads
    print("---- Extract Phase ----")
    run_data_fetching()

    # Step 2: Load raw data
    print("---- Load Phase ----")
    air_quality_df, respiratory_df = load_data()

    if air_quality_df is not None and respiratory_df is not None:
        # Step 3: Transform data using threads
        print("---- Transform Phase ----")
        air_quality_df, respiratory_df = run_transformations(air_quality_df, respiratory_df)

        # # Step 4: Merge datasets and save
        # print("---- Load Phase (Post-Transform) ----")
        # merged_df = merge_data(air_quality_df, respiratory_df)
        # save_data(merged_df, "merged_data.csv")

        print("Pipeline executed successfully. Data saved.")
    else:
        print("Pipeline terminated due to missing data.")


if __name__ == "__main__":
    main()
