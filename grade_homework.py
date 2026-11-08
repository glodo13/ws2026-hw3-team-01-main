import pytest
import os
from conftest import PointsReporter

def main():
    print("Starting the grader...\n")
    reporter = PointsReporter()
    
    # Get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Tell pytest to ONLY run tests found in this specific directory.
    pytest.main(["-v", script_dir], plugins=[reporter])
    
    reporter.summary()

if __name__ == "__main__":
    main()