# import pytest
from app.utilities import common as pl  # NoQA E402


def test_locale():
    assert pl.show_testing() == "TEST_DATA"  # "Should be TEST_DATA"


def test_sum():
    assert sum([1, 2, 3]) == 6  # "Should be 6"


def test_sum_tuple():
    assert sum((1, 2, 2)) == 5  # "Should be 5"

# End
