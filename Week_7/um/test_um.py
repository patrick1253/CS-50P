#CS50 assignment: 
    
# Ensure you have a correct version of um.py. Run your tests by executing pytest test_um.py. 
# pytest should show that all of your tests have passed.
    
# Modify the count function in the correct version of um.py. count might, for example, 
# mistakently also count any “um” that is part of a word. Run your tests by executing pytest 
# test_um.py. pytest should show that at least one of your tests has failed.
    
# Again modify the count function in the correct version of um.py. count might, for example, 
# mistakenly only match an “um” that is surrounded on either side by a space. Run your tests 
# by executing pytest test_um.py. pytest should show that at least one of your tests has failed.

from um import count

def main():
    test_count_commas()
    test_count_spaces()
    test_count_onlyUm()
    test_count_inWord()
    test_count_endOfLine()

def test_count_commas():
    assert count("um, hello, um, world") == 2

def test_count_spaces():
    assert count("um hello um world") == 2

def test_count_onlyUm():
    assert count("um") == 1

def test_count_inWord():
    assert count("the um album of um geraniums") == 2

def test_count_endOfLine():
    assert count("um?") == 1

if __name__ == "__main__":
    main()
