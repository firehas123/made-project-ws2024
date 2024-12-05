import os
import pytest
import pandas as pd
import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

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

    # Validate file content
    df = pd.read_csv(AIR_QUALITY_FILE)
    assert not df.empty, "Air Quality CSV file is empty."
    assert "state_code" in df.columns, "Expected column 'state_code' not found in Air Quality CSV."


def test_fetch_air_quality_data_failure():
    """
    Test fetch_air_quality_data function for failed API response.
    """
    mock_response = MagicMock()
    mock_response.status_code = 500
    mock_response.text = "Internal Server Error"

    with patch("codebase.fetch_air_quality.requests.get", return_value=mock_response):
        fetch_air_quality_data()

    # Ensure the file is not created
    assert not os.path.exists(AIR_QUALITY_FILE), "Air Quality CSV file was created despite API failure."


# def test_fetch_respiratory_data_successful():
#     """
#     Test fetch_respiratory_data function for successful API response.
#     """
#     mock_response = MagicMock()
#     mock_response.status_code = 200
#     mock_response.json = MagicMock(return_value=[
#         {"state_code": "06", "asthma_rate": "10.5", "date": "2023-01-01"},
#         {"state_code": "06", "asthma_rate": "12.0", "date": "2023-01-02"}
#     ])

#     with patch("codebase.fetch_respiratory.requests.get", return_value=mock_response):
#         fetch_respiratory_data()

#     # Check if the file is created
#     assert os.path.exists(RESPIRATORY_FILE), "Respiratory CSV file was not created."

#     # Validate file content
#     df = pd.read_csv(RESPIRATORY_FILE)
#     assert not df.empty, "Respiratory CSV file is empty."
#     assert "state_code" in df.columns, "Expected column 'state_code' not found in Respiratory CSV."


# def test_fetch_respiratory_data_failure():
#     """
#     Test fetch_respiratory_data function for failed API response.
#     """
#     mock_response = MagicMock()
#     mock_response.status_code = 500
#     mock_response.text = "Internal Server Error"

#     with patch("codebase.fetch_respiratory.requests.get", return_value=mock_response):
#         fetch_respiratory_data()

#     # Ensure the file is not created
#     assert not os.path.exists(RESPIRATORY_FILE), "Respiratory CSV file was created despite API failure."
