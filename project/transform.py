import threading
from transform_air_quality import preprocess_air_quality
from transform_respiratory import preprocess_respiratory_data, filter_relevant_topics


def run_transformations(air_quality_df, respiratory_df):
    """Run threads to transform both datasets."""
    print("Starting data transformations...")

    # Placeholder for transformed data
    air_quality_transformed = {"df": None}
    respiratory_transformed = {"df": None}

    # Air Quality transformation thread
    def transform_air_quality():
        air_quality_transformed["df"] = preprocess_air_quality(air_quality_df)

    # Respiratory transformation thread
    def transform_respiratory():
        filtered_df = filter_relevant_topics(respiratory_df)
        respiratory_transformed["df"] = preprocess_respiratory_data(filtered_df)

    # Create threads
    air_quality_thread = threading.Thread(target=transform_air_quality)
    respiratory_thread = threading.Thread(target=transform_respiratory)

    # Start threads
    air_quality_thread.start()
    respiratory_thread.start()

    # Wait for threads to complete
    air_quality_thread.join()
    respiratory_thread.join()

    print("Data transformations complete.")
    return air_quality_transformed["df"], respiratory_transformed["df"]

