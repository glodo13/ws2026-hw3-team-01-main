import pytest
import conversion

# This module is worth 1 point in total.

@pytest.mark.points(0.5)
def test_celsius2fahrenheit():
    """Tests the Celsius to Fahrenheit conversion."""
    assert conversion.celsius2fahrenheit(0) == 32
    assert conversion.celsius2fahrenheit(31) == pytest.approx(87.8)
    assert conversion.celsius2fahrenheit(-12) == pytest.approx(10.4)

@pytest.mark.points(0.5)
def test_fahrenheit2celsius():
    """Tests the Fahrenheit to Celsius conversion."""
    assert conversion.fahrenheit2celsius(0) == pytest.approx(-32 / 1.8)
    assert conversion.fahrenheit2celsius(32) == 0
    assert conversion.fahrenheit2celsius(99.2) == pytest.approx(67.2 / 1.8)

if __name__ == "__main__":
    from conftest import PointsReporter
    reporter = PointsReporter()
    pytest.main(["-v", __file__], plugins=[reporter])
    reporter.summary()
