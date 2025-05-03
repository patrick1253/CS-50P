# CS50 assignment: # Either before or after you implement validate in numb3rs.py, additionally implement, in a 
# file called test_numb3rs.py, two or more functions that collectively test your implementation 
# of validate thoroughly, each of whose names should begin with test_ so that you can execute your 
# tests with: pytest test_numb3rs.py

from numb3rs import validate
from random import randint

def main():
    test_validate_not4groups()
    test_validate_notInRange()
    test_validate_notDigits()
    test_validate_correctFormat()


def test_validate_not4groups():
    ip_groups = []
    for i in range(3):
        ip_groups.append(str(randint(0, 255)))
    assert validate(f"{ip_groups[0]}.{ip_groups[1]}.{ip_groups[2]}") == "Invalid"


def test_validate_notInRange():
    ip_groups = []
    for i in range(4):
        ip_groups.append(str(randint(255, 1000)))
    assert validate(f"{ip_groups[0]}.{ip_groups[1]}.{ip_groups[2]}.{ip_groups[3]}") == "Invalid"
    

def test_validate_notDigits():
    assert validate("cat") == "Invalid"


def test_validate_correctFormat():
    ip_groups = []
    for i in range(4):
        ip_groups.append(str(randint(0, 255)))
    assert validate(f"{ip_groups[0]}.{ip_groups[1]}.{ip_groups[2]}.{ip_groups[3]}") == "Valid"


if __name__ == "__main__":
    main()