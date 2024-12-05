import pandas as pd
import requests

def fetch_respiratory_data():
    """Fetch respiratory data and save to CSV."""
    print("Starting Respiratory Data")
    
    # API Endpoint and Parameters
    url = "https://data.cdc.gov/resource/hksd-2xuw.json"
    params = {
        "$limit": 1000,  # Fetch 1,000 rows at a time
        "$offset": 0
        # ,    # Start from the beginning
        # "$where": "topic='Asthma'",  # Filter for respiratory-related topic
        # "$$app_token": "YOUR_APP_TOKEN"  # Replace with your Socrata App Token if required
    }

    all_data = []
    while True:
        response = requests.get(url, params=params)
        if response.status_code != 200:
            print(f"Error: {response.status_code}, {response.text}")
            break

        data = response.json()
        if not data:
            break  # No more data to fetch

        all_data.extend(data)
        print(f"Fetched {len(all_data)} rows so far for Respiratory")

        # Increment offset for next batch
        params["$offset"] += 1000

    # Convert data to DataFrame and Save
    if all_data:
        df = pd.DataFrame(all_data)
        csv_file = "respiratory_data.csv"
        df.to_csv(csv_file, index=False)
        print(f"Respiratory data saved to {csv_file}")
    else:
        print("No data fetched.")

if __name__ == "__main__":
    fetch_respiratory_data()
