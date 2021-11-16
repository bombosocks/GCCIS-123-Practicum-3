"""
Test for study 3
"""

from study3 import *

def test_make_tuple():
    tuple = make_tuple("a", 1, 2)
    assert ("a", 1, 2) == tuple

def test_reverse_tuple():
    a_list = ["a", 1, "b"]
    a_tuple = (1, "b", 3)

    assert ("b", 1, "a") == reverse_tuple(a_list)
    assert (3, "b", 1) == reverse_tuple(a_tuple)