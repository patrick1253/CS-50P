#CS50 Assignemnt: Either before or after you implement convert in working.py, additionally 
# implement, in a file called test_working.py, three or more functions that collectively 
# test your implementation of convert thoroughly, each of whose names should begin with test_ 
# so that you can execute your tests with:  pytest test_working.py

from working import convert
from random import randint
import pytest

def main():
    test_convert_hourOver12()
    test_convert_minOver59()
    test_convert_noAMPM()
    test_convert_noMins()
    test_convert_correct()

def test_convert_hourOver12():
    with pytest.raises(SystemExit):
         convert(f"{randint(13, 23)}:{randint(0, 59)}PM to {randint(13, 23)}:{randint(0, 59)}PM") 


def test_convert_minOver59():
    with pytest.raises(SystemExit):
        convert(f"{randint(0, 12)}:{randint(60, 99)}PM to {randint(0, 12)}:{randint(60, 99)}PM") 


def test_convert_noAMPM():
    with pytest.raises(SystemExit):
        convert(f"{randint(0, 12)}:{randint(0, 59)} to {randint(0, 12)}:{randint(0, 59)}") 

def test_convert_noMins():
        assert convert("9 AM to 11 AM") == "9:00 to 11:00"

def test_convert_correct():
        assert convert("9:00 AM to 11:00 AM") == "9:00 to 11:00"
