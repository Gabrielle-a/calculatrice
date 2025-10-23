import math
import pytest
from src import utils

def test_add_basic():
    assert utils.add(1, 2, 3) == 6

def test_add_empty():
    assert utils.add() == 0

def test_subtract_basic():
    assert utils.subtract(10, 3, 2) == 5

def test_subtract_requires_one():
    with pytest.raises(ValueError):
        utils.subtract()

def test_multiply_basic():
    assert utils.multiply(4, 5) == 20

def test_divide_basic():
    assert utils.divide(9, 3) == 3

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        utils.divide(1, 0)

def test_divide_float():
    assert math.isclose(utils.divide(1, 4), 0.25)
