import pytest
from app import *

def test_valid_line():
    line = '190: 10 19'
    assert validate_line(line) is True

def test_invalid_line():
    line = '21037: 9 7 18 13'
    assert validate_line(line) is False

def test_valid_line_left_to_right():
    line = '292: 11 6 16 20'
    assert validate_line(line) is True
