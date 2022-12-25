# import pytest
from app.utilities import common as pll  # NoQA E402


def test_sum():
    assert sum([1, 2, 3]) == 6  # "Should be 6"


def test_sum_tuple():
    assert sum((1, 2, 2)) == 5  # "Should be 5"


def test_valid_map():
    assert pll.check_map(pll.map) is True  # "Should be True"
# End
