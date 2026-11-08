import pytest
import business

# This module is worth 1 point in total.

@pytest.mark.points(0.5)
def test_interest():
    """Tests the interest calculation function."""
    assert business.interest(100, 0.1) == pytest.approx(10)
    assert business.interest(100, 0.1, tax=0.2) == pytest.approx(8)
    assert business.interest(100, 0.1, 2) == pytest.approx(21)
    assert business.interest(100, 0.1, 2, 0.2) == pytest.approx(16.64)

@pytest.mark.points(0.5)
def test_terminal_value():
    """Tests the terminal value calculation function."""
    assert business.terminal_value(100, 0.1) == pytest.approx(110)
    assert business.terminal_value(100, 0.1, tax=0.2) == pytest.approx(108)
    assert business.terminal_value(100, 0.1, 2) == pytest.approx(121)
    assert business.terminal_value(100, 0.1, 2, 0.2) == pytest.approx(116.64)

if __name__ == "__main__":
    from conftest import PointsReporter
    reporter = PointsReporter()
    pytest.main(["-v", __file__], plugins=[reporter])
    reporter.summary()
