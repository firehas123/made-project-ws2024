import pandas as pd
import requests
import json

url = "https://aqs.epa.gov/data/api/sampleData/byState"
params = {
    "email": "mr.hassanch@gmail.com",
    "key": "aquafrog82",  # Replace with your actual API key
    "param": "88101",  # PM2.5 parameter code
    "bdate": "20230101",  # Begin date
    "edate": "20230131",  # End date
    "state": "06"  # California FIPS code
}

response = requests.get(url, params=params)

if response.status_code == 200:
    response_json = json.loads(response.text)
    
    # Check for API failure
    if response_json.get("status") == "Failed":
        print(f"API Request Failed: {response_json.get('error')}")
    else:
        # Extract data
        data = response_json.get("Data", [])
        if data:
            df = pd.DataFrame(data)
            
            # Save to CSV
            csv_file = "air_quality_data.csv"
            df.to_csv(csv_file, index=False)
            print(f"Data saved to {csv_file}")
        else:
            print("No data found in the API response.")
else:
    print(f"Error: {response.status_code}, {response.text}")
