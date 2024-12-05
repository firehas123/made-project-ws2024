import pandas as pd
import requests
import json

def fetch_air_quality_data():
    """Fetch air quality data and save it to CSV."""
    url = "https://aqs.epa.gov/data/api/sampleData/byState"
    params = {
        "email": "mr.hassanch@gmail.com",
        "key": "aquafrog82",  # Replace with your actual API key
        "param": "88101",  # PM2.5 parameter code
        "bdate": "20230101",  # Begin date
        "edate": "20230131",  # End date
        "state": "06"  # California FIPS code
    }
    print("Starting Air Quality Data")
    response = requests.get(url, params=params)

    if response.status_code == 200:
        response_json = json.loads(response.text)
        if response_json.get("status") == "Failed":
            print(f"Air Quality API Request Failed: {response_json.get('error')}")
        else:
            data = response_json.get("Data", [])
            if data:
                df = pd.DataFrame(data)
                print(f"Fetched {len(df)} rows for Air Quality data.")  # Row count message
                csv_file = "air_quality_data.csv"
                df.to_csv(csv_file, index=False)
                print(f"Air quality data saved to {csv_file}")
            else:
                print("No data found in the air quality API response.")
    else:
        print(f"Error fetching air quality data: {response.status_code}, {response.text}")

if __name__ == "__main__":
    fetch_air_quality_data()