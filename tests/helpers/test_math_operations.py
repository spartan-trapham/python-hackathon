import unittest
from src.helpers.math_operations import add

def test_add():
    assert add(3, 4) == 7
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
