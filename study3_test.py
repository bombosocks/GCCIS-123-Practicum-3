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

def test_make_list():
    assert ["bruh", 1, 42] == make_list("bruh", 1, 42)

def test_nth_list():
    a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert [2, 4, 6, 8, 10] == nth_list(a_list, 2)

def test_odds_before_evens():
    assert [1, 3, 5, 7, 9, 2, 4, 6, 8, 10] == odds_before_evens([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# I am skipping some tests as I just wanna get through this and they're unecesary

