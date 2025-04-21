# CS50 assignment:In a file called twttr.py, reimplement Setting up my twttr 
# from Problem Set 2, restructuring your code per the below, wherein shorten expects 
# a str as input and returns that same str but with all vowels (A, E, I, O, and U) 
# omitted, whether inputted in uppercase or lowercase.

# Then, in a file called test_twttr.py, implement one or more functions that collectively 
# test your implementation of shorten thoroughly, each of whose names should begin with 
# test_ so that you can execute your tests with: "pytest test_twttr.py"

from twttr_buggy import shorten
#import pytest

#def main():

def test_shorten_lowercase():
    word = "this is a test message in all lower case"
    assert shorten(word) == "ths s  tst mssg n ll lwr cs"

def test_shorten_uppercase():
    word = "THIS IS A TEST MESSAGE IN ALL UPPER CASE"
    assert shorten(word) == "THS S  TST MSSG N LL PPR CS"

def test_shorten_numeric_str():
    word = "12345"
    assert shorten(word) == "12345"


#if __name__=="__main__":
#    main()