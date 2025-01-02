import threading
from codebase.fetch_air_quality import fetch_air_quality_data
from codebase.fetch_respiratory import fetch_respiratory_data


def run_data_fetching():
    """Run threads to fetch data."""
    print("Starting data fetching...")
    air_quality_thread = threading.Thread(target=fetch_air_quality_data)
    # respiratory_thread = threading.Thread(target=fetch_respiratory_data)

    # Start both threads
    air_quality_thread.start()
    # respiratory_thread.start()

    # Wait for both threads to finish
    air_quality_thread.join()
    # respiratory_thread.join()
    print("Data fetching complete.")
