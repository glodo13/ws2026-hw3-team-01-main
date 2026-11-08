import pytest
from math import hypot
import os
import vrptw_reader

# This module is worth 2 points in total.

# --- NEW: A SINGLE, ROBUST FIXTURE ---
@pytest.fixture(scope="module")
def vrptw_context(request):

    # Step 1: Determine the correct directory
    student_dir_from_env = os.environ.get('STUDENT_PATH')
    if student_dir_from_env:
        # MASTER GRADER MODE
        data_dir = student_dir_from_env
    else:
        # LOCAL/STUDENT MODE
        data_dir = str(request.fspath.dirpath())

    # Step 2: Check for required files
    required_files = ['r101.txt', 'r102.txt']
    for filename in required_files:
        if not os.path.exists(os.path.join(data_dir, filename)):
            pytest.skip(f"Data file '{filename}' not found. Skipping all vrptw_reader tests.")

    # Step 3: Change directory and run tests
    original_cwd = os.getcwd()
    os.chdir(data_dir)
    yield data_dir  # The 'yield' provides the path to the tests if needed
    
    # Step 4: Clean up
    os.chdir(original_cwd)


# --- Part 1 Tests ---
# All tests in this section will use the vrptw_context fixture.
@pytest.mark.usefixtures("vrptw_context")
class TestVrptwPart1:
    # Grouping tests in a class makes applying fixtures cleaner.
    
    @pytest.mark.points(0.25)
    def test_read_string_list_default(self):
        """Test default instance name."""
        strings = vrptw_reader.read_string_list()
        strings2 = vrptw_reader.read_string_list('r101')
        assert strings == strings2

    @pytest.mark.points(0.25)
    def test_read_string_list_extension(self):
        """Test automatic addition of filename extension."""
        strings = vrptw_reader.read_string_list('r102')
        strings2 = vrptw_reader.read_string_list('r102.txt')
        assert strings == strings2

    @pytest.mark.points(0.25)
    def test_read_string_list_count(self):
        """Test if the correct number of entries is read."""
        strings = vrptw_reader.read_string_list('r101')
        assert len(strings) == 101

    @pytest.mark.points(0.25)
    def test_read_string_list_data_correctness(self):
        """Test if data is read correctly."""
        n1 = '    1      35.00      35.00       0.00       0.00     230.00       0.00\n'
        n7 = '    7      25.00      30.00       3.00      99.00     109.00      10.00\n'
        n101 = '  101      18.00      18.00      17.00     185.00     195.00      10.00\n'
        strings = vrptw_reader.read_string_list('r102')
        assert strings[0] == n1
        assert strings[6] == n7
        assert strings[100] == n101


# --- Part 2 Tests ---
@pytest.mark.usefixtures("vrptw_context")
class TestVrptwPart2:
    
    @pytest.fixture(scope="class")
    def r101_strings(self):
        """Loads the r101 data once for all tests in this class."""
        return vrptw_reader.read_string_list('r101')

    @pytest.mark.points(0.5)
    def test_get_demand(self, r101_strings):
        """Tests the get_demand function."""
        assert vrptw_reader.get_demand(r101_strings, 1) == 0.0
        assert vrptw_reader.get_demand(r101_strings, 9) == 9.0
        assert vrptw_reader.get_demand(r101_strings, 101) == 17.0

    @pytest.mark.points(0.5)
    def test_calc_distance(self, r101_strings):
        """Tests the calc_distance function."""
        assert vrptw_reader.calc_distance(r101_strings, 1, 3) == pytest.approx(18.0)
        assert vrptw_reader.calc_distance(r101_strings, 1, 17) == pytest.approx(hypot(25, 15))


# --- This part for local execution remains the same ---
if __name__ == "__main__":
    from conftest import PointsReporter
    reporter = PointsReporter()
    pytest.main(["-v", __file__], plugins=[reporter])
    reporter.summary()

