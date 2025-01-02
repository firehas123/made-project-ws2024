# Air Quality API URL

API_URL = "https://aqs.epa.gov/data/api/sampleData/byState"
API_PARAMS = {
    "email": "mr.hassanch@gmail.com",
    "key": "berrymouse39",  # Replace with your actual API key
    "param": "88101",  # PM2.5 parameter code
    "bdate": "20190101",  # Begin date
    "edate": "20190131",  # End date
    "state": "06"  # California FIPS code
}

FILENAME = "air_quality_data1.csv"


# Respiratory API URL

RESPIRATORY_API_URL = "https://data.cdc.gov/resource/hksd-2xuw.json"

RESPIRATORY_API_PARAMS = {
    "$limit": 1000,  # Fetch 1,000 rows at a time
    "$offset": 0,    # Start from the beginning
    # "$where": "topic='Asthma'",  # Uncomment if filtering is needed
    # "$$app_token": "YOUR_APP_TOKEN"  # Replace with your Socrata App Token if required
}

CSV_FILE_RESPIRATORY = "respiratory_data.csv"