# CS50 assignment:  voluntarily adding a unit test for lines_alt.py, just to practice.

#from lines_alt import valid_file, count_lines
import lines_alt 
import pytest

def test_lines_alt_noPyExt():
    with pytest.raises(NameError):
        lines_alt("['lines_alt.py', 'lines']")

def test_lines_alt_correct():
    assert count_lines("lines.py") == "27"