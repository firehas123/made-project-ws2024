import pandas as pd
import requests

# Import the configuration
from codebase.config import API_URL, API_PARAMS, FILENAME


def fetch_air_quality_data():
    """
    Fetch air quality data from the API and save it to a CSV.
    """
    try:
        print("Starting Air Data Fetch...")
        response = requests.get(API_URL, params=API_PARAMS)
        print(f"API request sent to {API_URL} with params {API_PARAMS}")
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx, 5xx)
        response_json = response.json()

        # Check if the API request was successful
        if response_json.get("status") == "Failed":
            print(f"API Request Failed: {response_json.get('error')}")
        
        # Save the data
        if "Data" in response_json:
            print("Saving data to CSV...")
            save_to_csv(response_json["Data"])
        else:
            print("No 'Data' key found in the API response.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def save_to_csv(data, filename=FILENAME):
    """
    Save the data to a CSV file.
    """
    try:
        if data:
            print("Converting data to DataFrame...")
            df = pd.DataFrame(data)
            print(f"Saving DataFrame to {filename}...")
            df.to_csv(filename, index=False)
            print(f"Data successfully saved to {filename}")
        else:
            print("No data found to save. Data is empty or None.")
    except Exception as e:
        print(f"Error saving data to CSV: {e}")
