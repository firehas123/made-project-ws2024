import threading
from fetch_air_quality import fetch_air_quality_data
from fetch_respiratory import fetch_respiratory_data

if __name__ == "__main__":
    # Create threads for fetching air quality and respiratory data
    air_quality_thread = threading.Thread(target=fetch_air_quality_data)
    respiratory_thread = threading.Thread(target=fetch_respiratory_data)

    # Start the threads
    air_quality_thread.start()
    respiratory_thread.start()

    # Wait for both threads to complete
    air_quality_thread.join()
    respiratory_thread.join()

    print("Data fetching complete. You can now run your pipeline.")
