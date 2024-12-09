import pandas as pd
import requests
import json
import sys
from pathlib import Path

# Add the parent directory to sys.path to import config.py
sys.path.append(str(Path(__file__).resolve().parent.parent))

# Import the configuration
from config import API_URL, API_PARAMS, FILENAME


def fetch_air_quality_data():
    try:
        response = requests.get(API_URL, params=API_PARAMS, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx, 5xx)
        response_json = response.json()
        
        # Check API response for status
        if response_json.get("status") == "Failed":
            print(f"API Request Failed: {response_json.get('error')}")
            return None
        return response_json
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def save_to_csv(data, filename=FILENAME):
    if data:
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
    else:
        print("No data found to save.")


if __name__ == "__main__":
    # Fetch air data using constants directly
    response_data = fetch_air_quality_data()
    
    if response_data and "Data" in response_data:
        data = response_data["Data"]
        save_to_csv(data)
    else:
        print("No data fetched or invalid response.")
