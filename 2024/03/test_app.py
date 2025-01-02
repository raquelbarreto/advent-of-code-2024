import pytest
from app import *

def test_valid_instructions():
    string = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
    assert find_valid_instructions(string) == [(2, 4), (5, 5), (11, 8), (8, 5)]

    string = 'xmul(3,477777)%&mul[3,xx]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
    assert find_valid_instructions(string) == [(5, 5), (11, 8), (8, 5)]


