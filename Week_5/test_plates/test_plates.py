# CS50 assignment: In a file called plates.py, reimplement Vanity Plates from 
# Problem Set 2, restructuring your code per the below, wherein is_valid still 
# expects a str as input and returns True if that str meets all requirements 
# and False if it does not.

# Then, in a file called test_plates.py, implement four or more functions that 
# collectively test your implementation of is_valid thoroughly, each of whose names 
# should begin with test_ so that you can execute your tests with: "pytest test_plates.py"

from plates import is_valid

def test_is_valid_tooshort():
    assert is_valid("c") == "Invalid"


def test_is_valid_toolong():
    assert is_valid("TooLong") == "Invalid"


def test_is_valid_firstcharnumber():
    assert is_valid("2Shy") == "Invalid"


def test_is_valid_midcharnumbers():
    assert is_valid("H2O") == "Invalid"


def test_is_valid_firstnumberzero():
    assert is_valid("IM007") == "Invalid"


def test_is_valid_correct():
    assert is_valid("Works") == "Valid"