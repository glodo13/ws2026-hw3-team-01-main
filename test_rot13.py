import pytest
import rot13

# This module is worth 1 point in total.

@pytest.fixture
def test_strings():
    """Provides test strings for encoding/decoding."""
    return {
        "plain": "Never trust a program you don't have sources for.",
        "encoded": "Arire gehfg n cebtenz lbh qba'g unir fbheprf sbe."
    }

@pytest.mark.points(0.5)
def test_encode(test_strings):
    """Tests the ROT13 encode function."""
    assert rot13.encode('') == ''
    assert rot13.encode(rot13.encode('test')) == 'TEST'
    assert rot13.encode(test_strings["plain"]) == test_strings["encoded"].upper()
    assert rot13.encode(test_strings["encoded"]) == test_strings["plain"].upper()

@pytest.mark.points(0.5)
def test_decode(test_strings):
    """Tests the ROT13 decode function."""
    assert rot13.decode('') == ''
    assert rot13.decode(rot13.decode('test')) == 'TEST'
    assert rot13.decode(test_strings["plain"]) == test_strings["encoded"].upper()
    assert rot13.decode(test_strings["encoded"]) == test_strings["plain"].upper()

if __name__ == "__main__":
    from conftest import PointsReporter
    reporter = PointsReporter()
    pytest.main(["-v", __file__], plugins=[reporter])
    reporter.summary()
