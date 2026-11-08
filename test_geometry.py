import pytest
from math import hypot, pi
import geometry

# This module is worth 1 point in total, divided among 10 tests.

@pytest.mark.points(0.1)
def test_perimeter_right_triangle():
    assert geometry.perimeter_right_triangle(0, 0) == 0.0
    assert geometry.perimeter_right_triangle(4, 3) == 12.0

@pytest.mark.points(0.1)
def test_area_right_triangle():
    assert geometry.area_right_triangle(0, 0) == 0.0
    assert geometry.area_right_triangle(4, 3) == 6.0

@pytest.mark.points(0.1)
def test_perimeter_circle():
    assert geometry.perimeter_circle(0) == pytest.approx(0.0)
    assert geometry.perimeter_circle(1) == pytest.approx(2 * pi)
    assert geometry.perimeter_circle(2.5) == pytest.approx(2.5 * 2 * pi)

@pytest.mark.points(0.1)
def test_area_circle():
    assert geometry.area_circle(0) == pytest.approx(0.0)
    assert geometry.area_circle(1) == pytest.approx(pi)
    assert geometry.area_circle(2.5) == pytest.approx(2.5 * 2.5 * pi)

@pytest.mark.points(0.1)
def test_surface_sphere():
    assert geometry.surface_sphere(0) == pytest.approx(0.0)
    assert geometry.surface_sphere(1) == pytest.approx(4 * pi)
    assert geometry.surface_sphere(2.5) == pytest.approx(4 * pi * 2.5 * 2.5)

@pytest.mark.points(0.1)
def test_volume_sphere():
    assert geometry.volume_sphere(0) == pytest.approx(0.0)
    assert geometry.volume_sphere(1) == pytest.approx(4 / 3 * pi)
    assert geometry.volume_sphere(2.5) == pytest.approx(4 / 3 * pi * 2.5**3)

@pytest.mark.points(0.1)
def test_surface_cylinder():
    assert geometry.surface_cylinder(0, 0) == pytest.approx(0.0)
    assert geometry.surface_cylinder(1, 0) == pytest.approx(2 * pi)
    assert geometry.surface_cylinder(0, 1) == pytest.approx(0.0)
    assert geometry.surface_cylinder(1, 1) == pytest.approx(4 * pi)
    assert geometry.surface_cylinder(2.2, 3) == pytest.approx(2 * 2.2 * 2.2 * pi + 2 * 2.2 * pi * 3)

@pytest.mark.points(0.1)
def test_volume_cylinder():
    assert geometry.volume_cylinder(0, 0) == pytest.approx(0.0)
    assert geometry.volume_cylinder(1, 0) == pytest.approx(0.0)
    assert geometry.volume_cylinder(0, 1) == pytest.approx(0.0)
    assert geometry.volume_cylinder(1, 1) == pytest.approx(pi)
    assert geometry.volume_cylinder(2.2, 3.1) == pytest.approx(2.2 * 2.2 * pi * 3.1)

@pytest.mark.points(0.1)
def test_surface_cone():
    assert geometry.surface_cone(0, 0) == pytest.approx(0.0)
    assert geometry.surface_cone(0, 1) == pytest.approx(0.0)
    assert geometry.surface_cone(1, 1) == pytest.approx(pi + hypot(1, 1) * pi)
    assert geometry.surface_cone(2.2, 3.1) == pytest.approx(2.2 * 2.2 * pi + 2.2 * pi * hypot(2.2, 3.1))

@pytest.mark.points(0.1)
def test_volume_cone():
    assert geometry.volume_cone(0, 0) == pytest.approx(0.0)
    assert geometry.volume_cone(1, 0) == pytest.approx(0.0)
    assert geometry.volume_cone(0, 1) == pytest.approx(0.0)
    assert geometry.volume_cone(1, 1) == pytest.approx(pi / 3.0)
    assert geometry.volume_cone(2.2, 3.1) == pytest.approx(2.2 * 2.2 * pi * 3.1 / 3.0)

if __name__ == "__main__":
    from conftest import PointsReporter
    reporter = PointsReporter()
    pytest.main(["-v", __file__], plugins=[reporter])
    reporter.summary()
