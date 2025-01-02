import pandas as pd
import requests
from codebase.config import API_URL, API_PARAMS, FILENAME


def fetch_air_quality_data():
    """
    Fetch air quality data for each year in the specified range and merge them into a single CSV file.
    """
    try:
        print("Starting Air Data Fetch...")
        bdate = API_PARAMS.get("bdate")
        edate = API_PARAMS.get("edate")

        if bdate and edate:
            bdate =  pd.to_datetime(bdate, format='%Y')
            edate = pd.to_datetime(edate, format='%Y')
            years = edate.year - bdate.year
            print(f"Fetching data for {years + 1} years from {bdate.year} to {edate.year}...")
            all_data = pd.DataFrame()

            for year in range(bdate.year, edate.year + 1):
                API_PARAMS["bdate"] = f"{year}0101"
                API_PARAMS["edate"] = f"{year}1231"
                print(f"Fetching data for {year}...")
                print(f"API request sent to {API_URL} with params {API_PARAMS}")

                response = requests.get(API_URL, params=API_PARAMS)
                
                response.raise_for_status()                
                response_json = response.json()
                print("data fetched")
                if "Data" in response_json:
                    yearly_data = pd.DataFrame(response_json["Data"])
                    all_data = pd.concat([all_data, yearly_data], ignore_index=True)
                else:
                    print(f"No data found for {year}.")

            if not all_data.empty:
                print("Saving data to CSV...")
                save_to_csv(all_data)
            else:
                print("No data found to save.")
        
        else:
            response = requests.get(API_URL, params=API_PARAMS)
            print(f"API request sent to {API_URL} with params {API_PARAMS}")
            response.raise_for_status()
            response_json = response.json()

            if "Data" in response_json:
                print("Saving data to CSV...")
                save_to_csv(response_json["Data"])
            else:
                print("No 'Data' key found in the API response.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")


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