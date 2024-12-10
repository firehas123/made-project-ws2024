import pandas as pd
import requests

# Import configurations
from config import RESPIRATORY_API_URL, RESPIRATORY_API_PARAMS, CSV_FILE_RESPIRATORY

def fetch_respiratory_data():
    """Fetch respiratory data and save to CSV."""
    print("Starting Respiratory Data Fetch")
    
    # Copy API parameters to avoid modifying the original
    params = RESPIRATORY_API_PARAMS.copy()

    all_data = []
    while True:
        response = requests.get(RESPIRATORY_API_URL, params=params)
        if response.status_code != 200:
            print(f"Error: {response.status_code}, {response.text}")
            break

        data = response.json()
        if not data:
            break  # No more data to fetch

        all_data.extend(data)
        print(f"Fetched {len(all_data)} rows so far for Respiratory")

        # Increment offset for the next batch
        params["$offset"] += 1000

    # Convert data to DataFrame and save
    if all_data:
        df = pd.DataFrame(all_data)
        df.to_csv(CSV_FILE_RESPIRATORY, index=False)
        print(f"Respiratory data saved to {CSV_FILE_RESPIRATORY}")
    else:
        print("No data fetched.")

if __name__ == "__main__":
    fetch_respiratory_data()
