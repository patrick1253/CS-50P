# CS50 assignment: In a file called bank.py, reimplement Home Federal Savings Bank 
# from Problem Set 1, restructuring your code per the below, wherein value expects 
# a str as input and returns an int, namely 0 if that str starts with “hello”, 20 if 
# that str starts with an “h” (but not “hello”), or 100 otherwise, treating the str 
# case-insensitively. You can assume that the string passed to the value function will n
# ot contain any leading spaces. Only main should call print.

# Then, in a file called test_bank.py, implement three or more functions that collectively 
# test your implementation of value thoroughly, each of whose names should begin with test_ 
# so that you can execute your tests with: "pytest test_bank.py"

from bank import value


def test_value_hello():
    assert value("hello") == 0


def test_value_hi():
    assert value("hi") == 20


def test_value_morning():
    assert value("good morning") == 100