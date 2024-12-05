import pytest
import os

def run_tests():
    """
    Parent test runner that executes all individual tests in the tests/ directory.
    """
    print("Running all ETL tests...")

    # Directory containing individual test modules
    tests_dir = os.path.join(os.path.dirname(__file__), "tests")

    # Run pytest on all files in the tests directory
    pytest_args = [tests_dir, "-v"]
    pytest.main(pytest_args)


if __name__ == "__main__":
    run_tests()
