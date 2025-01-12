import pandas as pd
import requests
from datetime import datetime, timedelta
import time

# Import the configuration
from codebase.config import API_URL, API_PARAMS, FILENAME

def fetch_air_quality_data():
    """
    Fetch air quality data incrementally (monthly) and merge into a single CSV file.
    """
    try:
        print("Starting Air Data Fetch...")
        bdate = API_PARAMS.get("bdate")
        edate = API_PARAMS.get("edate")
        
        if bdate and edate:
            bdate = pd.to_datetime(bdate, format='%Y%m%d')
            edate = pd.to_datetime(edate, format='%Y%m%d')
            
            current_date = bdate
            all_data = pd.DataFrame()
            
            while current_date <= edate:
                next_date = (current_date + pd.DateOffset(months=1)) - timedelta(days=1)
                if next_date > edate:
                    next_date = edate
                
                API_PARAMS["bdate"] = current_date.strftime('%Y%m%d')
                API_PARAMS["edate"] = next_date.strftime('%Y%m%d')
                
                print(f"Fetching data from {API_PARAMS['bdate']} to {API_PARAMS['edate']}...")
                response = requests.get(API_URL, params=API_PARAMS)
                
                response.raise_for_status()                
                response_json = response.json()
                
                if "Data" in response_json:
                    chunk_data = pd.DataFrame(response_json["Data"])
                    all_data = pd.concat([all_data, chunk_data], ignore_index=True)
                    print(f"Data for {API_PARAMS['bdate']} to {API_PARAMS['edate']} fetched successfully.")
                else:
                    print(f"No data found from {API_PARAMS['bdate']} to {API_PARAMS['edate']}. Moving to next window.")
                
                current_date = next_date + timedelta(days=1)
                print("Pausing for 1 minutes to avoid API limits...")
                time.sleep(60)  # Pause for 1 minutes
            
            # Append all data to CSV after loop ends
            append_to_csv(all_data)
        else:
            print("No valid start or end date provided in API_PARAMS.")
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def append_to_csv(data, filename=FILENAME):
    """
    Append data to an existing CSV file or create a new one if it doesn't exist.
    """
    try:
        if not data.empty:
            write_header = not pd.io.common.file_exists(filename)
            data.to_csv(filename, mode='a', index=False, header=write_header)
            print(f"Data appended to {filename}.")
        else:
            print("No data to append.")
    except Exception as e:
        print(f"Error appending data to CSV: {e}")
