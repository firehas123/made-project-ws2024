import os
import pytest
import pandas as pd
from unittest.mock import patch, MagicMock
from codebase.fetch_air_quality import fetch_air_quality_data
from codebase.fetch_respiratory import fetch_respiratory_data

# File paths for output files
AIR_QUALITY_FILE = "air_quality_data.csv"
RESPIRATORY_FILE = "respiratory_data.csv"


@pytest.fixture(autouse=True)
def cleanup_files():
    """
    Cleanup files after each test to ensure a clean state.
    """
    yield
    for file in [AIR_QUALITY_FILE, RESPIRATORY_FILE]:
        if os.path.exists(file):
            os.remove(file)


def test_fetch_air_quality_data_successful():
    """
    Test fetch_air_quality_data function for successful API response.
    """
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = """
    {
        "status": "Success",
        "Data": [
            {"state_code": "06", "pm25": "15.0", "date": "2023-01-01"},
            {"state_code": "06", "pm25": "20.0", "date": "2023-01-02"}
        ]
    }
    """
    with patch("codebase.fetch_air_quality.requests.get", return_value=mock_response):
        fetch_air_quality_data()

    # Check if the file is created
    assert os.path.exists(AIR_QUALITY_FILE), "Air Quality CSV file was not created."
    df = pd.read_csv(AIR_QUALITY_FILE)
    assert len(df) > 0, "Air Quality CSV file is empty."


def test_fetch_respiratory_data_limit_500_rows():
    """
    Test fetch_respiratory_data function to fetch only the first 500 rows.
    """
    mock_data = [{"state_code": "06", "asthma_rate": f"{10.0 + i/100}", "date": f"2023-01-{(i % 30) + 1:02d}"} for i in range(1000)]

    def mock_get(url, params):
        offset = params.get("$offset", 0)
        if offset >= 500:
            return MagicMock(status_code=200, json=MagicMock(return_value=[]))
        return MagicMock(status_code=200, json=MagicMock(return_value=mock_data[offset:offset + 1000]))

    with patch("codebase.fetch_respiratory.requests.get", side_effect=mock_get):
        fetch_respiratory_data()

    assert os.path.exists(RESPIRATORY_FILE), "Respiratory CSV file was not created."
    df = pd.read_csv(RESPIRATORY_FILE)
    assert len(df) == 500, f"Expected 500 rows, but found {len(df)}."
