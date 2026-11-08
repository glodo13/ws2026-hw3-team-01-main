import pytest
import main

# This module is worth 1 point in total.

@pytest.mark.points(1.0)
def test_main():
    """Tests that the main function returns 0, indicating success."""
    assert main.main() == 0

if __name__ == "__main__":
    from conftest import PointsReporter
    reporter = PointsReporter()
    pytest.main(["-v", __file__], plugins=[reporter])
    reporter.summary()
