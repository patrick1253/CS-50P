# CS50 assignment: Either before or after you implement jar.py, additionally implement, 
# in a file called test_jar.py, four or more functions that collectively test your implementation 
# of Jar thoroughly, each of whose names should begin with test_ so that you can execute your 
# tests with: pytest test_jar.py

# Note that it’s not as easy to test instance methods as it is to test functions alone, since 
# instance methods sometimes manipulate the same “state” (i.e., instance variables). To test 
# one method (e.g., withdraw), then, you might need to call another method first (e.g., deposit). 
# But the method you call first might itself not be correct!


from jar import Jar


#def test_init():
#    ...


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar._size = 2
    jar.deposit(4)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪"
    
    

def test_withdraw():
    jar = Jar()
    jar._size = 10
    jar.withdraw(4)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪"
