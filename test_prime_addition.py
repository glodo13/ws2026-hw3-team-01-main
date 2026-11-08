import pytest
import prime_addition

# This module is worth 1 point in total.

@pytest.mark.points(0.34)
def test_prime_sum_simple():
    """Tests summing primes up to 0 and 1."""
    assert prime_addition.prime_sum_to(0) == 0
    assert prime_addition.prime_sum_to(1) == 0

@pytest.mark.points(0.33)
def test_prime_sum_regular():
    """Tests summing primes up to regular numbers."""
    assert prime_addition.prime_sum_to(10) == 17
    assert prime_addition.prime_sum_to(30) == 129

@pytest.mark.points(0.33)
def test_prime_sum_illegal():
    """Tests that negative inputs raise an AssertionError."""
    with pytest.raises(AssertionError):
        prime_addition.prime_sum_to(-1)
    with pytest.raises(AssertionError):
        prime_addition.prime_sum_to(-17)

if __name__ == "__main__":
    from conftest import PointsReporter
    reporter = PointsReporter()
    pytest.main(["-v", __file__], plugins=[reporter])
    reporter.summary()
