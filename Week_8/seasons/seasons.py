# CS50 assignment:  implement a program that prompts the user for their date of birth in 
# YYYY-MM-DD format and then sings prints how old they are in minutes, rounded to the nearest 
# integer, using English words instead of numerals, just like the song from Rent, without any 
# and between words. Since a user might not know the time at which they were born, assume, for 
# simplicity, that the user was born at midnight (i.e., 00:00:00) on that date. And assume that 
# the current time is also midnight. In other words, even if the user runs the program at noon, 
# assume that it’s actually midnight, on the same date. Use datetime.date.today to get today’s 
# date, per docs.python.org/3/library/datetime.html#datetime.date.today.

from datetime import date
import re, sys, inflect

p = inflect.engine()

def main():
    minutes = Season.get()
    #Lifetime.get()
    #DOB = input("Your date of birth in YYYY-MM-DD format: ")
    #minutes = convert_date(DOB)
    #Date.get()
    #Date.calc_minutes()
    print(f"You are", p.number_to_words(minutes, andword=''), f"minutes old!")
    #print(Season)
    
#def convert_date(DOB):
#    today = date.today()
#    timedelta = today - date.fromisoformat(DOB)
#    print(timedelta.days)
#    minutes = timedelta.days * 24 * 60
#    return minutes


class Season():
    #def __init__(self, DOB):
        #self.DOB = DOB    
    
    @property
    def DOB(cls):
        return cls._DOB
    
    @DOB.setter
    def DOB(cls, DOB):
        matches = re.fullmatch(r"^\d{4}-\d{2}-\d{2}$", DOB)
        if not matches:
            raise ValueError("Must be in YYYY-MM-DD format")
        cls._DOB = DOB


    @classmethod
    def get(cls):
        DOB = input("Your date of birth in YYYY-MM-DD format: ")
        matches = re.fullmatch(r"^\d{4}-\d{2}-\d{2}$", DOB)
        if not matches:
            sys.exit("Must be in YYYY-MM-DD format")
        cls._DOB = DOB     
        
        timedelta = date.today() - date.fromisoformat(cls._DOB)
        minutes = timedelta.days * 24 * 60
        return (minutes)

    def __str__(cls):
        return f"You are {cls.minutes} minutes old!"


    #def get():
        #DOB = input("Your date of birth in YYYY-MM-DD format: ")
        #timedelta = date.today() - date.fromisoformat(DOB)
        #lifetime = Lifetime(timedelta)
        #return lifetime


#class Date:
#    @classmethod
#    def get(cls):
#        #DOB = input("Your date of birth in YYYY-MM-DD format: ")

#        if not re.fullmatch(r"^\d{4}-\d{2}-\d{2}$", DOB):
#            raise ValueError("Must be in YYYY-MM-DD format")
#        cls._DOB = DOB


#    def calc_minutes(cls):
#        today = date.today()
#        timedelta = today - date.fromisoformat(cls._DOB)
#        minutes = timedelta.days * 24 * 60
#        return minutes

if __name__ == "__main__":
    main()
