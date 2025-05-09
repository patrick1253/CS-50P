# CS50 assignment: Suppose that you’d like to implement a cookie jar in which to store 
# cookies. In a file called jar.py, implement a class called Jar with these methods:

#    __init__ should initialize a cookie jar with the given capacity, which represents the 
# maximum number of cookies that can fit in the cookie jar. If capacity is not a non-negative 
# int, though, __init__ should instead raise a ValueError.
#    __str__ should return a str with # 🍪, where n is the number of cookies in the cookie jar. 
# 
# For instance, if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"
# deposit should add n cookies to the cookie jar. If adding that many would exceed the cookie jar’s 
# capacity, though, deposit should instead raise a ValueError.
# withdraw should remove n cookies from the cookie jar. Nom nom nom. If there aren’t that many 
# cookies in the cookie jar, though, withdraw should instead raise a ValueError.
# capacity should return the cookie jar’s capacity.
# size should return the number of cookies actually in the cookie jar, initially 0.

def main():
    jar = Jar(int(input("Jar capacity: ")))
    print("capacity: ", jar._capacity)
    jar.deposit(int(input("how many cookies do you want to deposit?")))
    jar.withdraw(n = int(input("how many cookies do you want to withdraw?")))
    print(jar.__str__())
    print("size: ", jar._size)

class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("capacity must be a positive integer")
        self._capacity = capacity


    def __str__(self):
        return f"🍪" * self.size
        #return f"Cookies in jar: " + "🍪" * self.size


    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("capacity of jar exceeded")
        self.size = self.size + n
        #print("self.size: ",  self.size)
        

    def withdraw(self, n):
        if self.size - n <= 0:
            raise ValueError("not enough cookies in jar")
        self.size = self.size - n
        #return self.size


    @property
    def size(self):
        return self._size
    
    @size.setter   
    def size(self, size):
        self._size = size


if __name__ == "__main__":
    main()