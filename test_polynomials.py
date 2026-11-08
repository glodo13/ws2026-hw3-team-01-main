import pytest
import polynomials

# This module is worth 1 point in total.

@pytest.mark.points(0.5)
def test_poly_simple():
    """Tests the polynomial evaluation with simple values."""
    coefficients = [4, 2, 9, 1]
    assert polynomials.eval_polynomial(coefficients, 0) == 4
    assert polynomials.eval_polynomial(coefficients, 4) == 220

@pytest.mark.points(0.5)
def test_poly_large():
    """Tests the polynomial evaluation with large values."""
    coefficients = [2, 7, 8, 1, 9]
    y = polynomials.eval_polynomial(coefficients, 424242424242)
    assert y == 291540498902294146068754588509689936340955257560

if __name__ == "__main__":
    from conftest import PointsReporter
    reporter = PointsReporter()
    pytest.main(["-v", __file__], plugins=[reporter])
    reporter.summary()