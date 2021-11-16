"""
Test for study 3
"""

from study3 import *

def test_make_tuple():
    tuple = make_tuple("a", 1, 2)
    assert ("a", 1, 2) == tuple