# CS50 assignment:  voluntarily adding a unit test for lines_alt.py, just to practice.

import lines_alt

def lines_alt_noPyExt():
    with pytest.raises(ValueError):
        lines_alt.valid_file("lines")

def lines_alt_correct():
    assert lines_alt.valid_file("lines.py") == "27"