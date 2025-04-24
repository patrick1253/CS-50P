# CS50 assignment: In a file called fuel.py, reimplement Fuel Gauge from Problem Set 3, 
# restructuring your code per the below, wherein:

#   Convert expects a str in X/Y format as input, wherein each of X and Y is an integer, 
#       and returns that fraction as a percentage rounded to the nearest int between 0 and 100, 
#       inclusive. If X and/or Y is not an integer, or if X is greater than Y, then convert 
#       should raise a ValueError. If Y is 0, then convert should raise a ZeroDivisionError.
#   Gauge expects an int and returns a str that is:
#        "E" if that int is less than or equal to 1,
#        "F" if that int is greater than or equal to 99,
#        and "Z%" otherwise, wherein Z is that same int.

# Then, in a file called test_fuel.py, implement two or more functions that collectively test 
# your implementations of convert and gauge thoroughly, each of whose names should begin with 
# test_ so that you can execute your tests with: "pytest test_fuel.py"

import fuel
import pytest

def test_convert_float():
    with pytest.raises(ValueError):
        fuel.convert("3.5/5")


def test_convert_Xgreater():
    with pytest.raises(ValueError):
        fuel.convert("6/5")


def test_convert_Yzero():
    with pytest.raises(ZeroDivisionError):
        fuel.convert("4/0")


def test_convert_notInt():
    with pytest.raises(ValueError):
        fuel.convert("m/5")


def test_gauge_notInt():
    with pytest.raises(ValueError):
        fuel.convert("3.5/5")


def test_convert_fullTank():
    assert fuel.convert("99/100") == "F"


def test_convert_emptyTank():
    assert fuel.convert("1/100") == "E"


def test_convert_correct():
    assert fuel.convert("3/4") == "75%"