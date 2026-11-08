"""
CONTEST FOR HOMEWORK 3 (FUNCTION-BASED GRADING)

This configuration is simplified because HW3 tests functions directly
instead of running scripts as subprocesses.

It contains the PointsReporter plugin for calculating scores.
This file can be used for both local testing and the master grader.
"""

import pytest

class PointsReporter:
    """The complete and correct PointsReporter plugin."""
    def __init__(self):
        self.achieved_points = 0.0
        self.total_possible_points = 0.0
        self.test_results = {}

    def pytest_configure(self, config):
        """Registers the custom 'points' marker to avoid warnings."""
        config.addinivalue_line("markers", "points(value): assign a custom point value")

    def pytest_collection_finish(self, session):
        """Calculates total points after all tests are collected."""
        self.achieved_points = 0.0
        self.total_possible_points = 0.0
        for item in session.items:
            marker = item.get_closest_marker("points")
            points = marker.args[0] if marker else 1.0
            self.total_possible_points += points
            self.test_results[item.nodeid] = {"points": points}
    
    def pytest_runtest_logreport(self, report):
        """Adds points for each passed test."""
        if report.when == 'call' and report.passed:
            nodeid = report.nodeid
            if nodeid in self.test_results:
                self.achieved_points += self.test_results[nodeid]["points"]

    def summary(self):
        """Prints the final, formatted score summary."""
        print("\n" + "="*40)
        # Round points for display to avoid floating point inaccuracies
        achieved_rounded = round(self.achieved_points, 4)
        total_rounded = round(self.total_possible_points, 4)
        print(f"   🏆 Final Score: {achieved_rounded} / {total_rounded} points 🏆")
        print("="*40)
