# AtBS chapter 4 

from comma import convert_list

def test_convert_list_none():
    assert convert_list("") == "List is empty"

def test_convert_list_one():
    assert convert_list("apple") == "apple"

def test_convert_list_two():
    assert convert_list("apple pear") == "apple and pear"

def test_convert_list_more():
    assert convert_list("apple pear tofu") == "apple, pear, and tofu"