# CS50 assignment:  implement a program that prompts the user for a time and outputs 
# whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, 
# don’t output anything at all. Assume that the user’s input will be formatted in 24-hour 
# time as #:## or ##:##. And assume that each meal’s time range is inclusive. For instance, 
# whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

# Structure your program per the below, wherein convert is a function (that can be called by main) 
# that converts time, a str in 24-hour format, to the corresponding number of hours as a float. 
# For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 
# (i.e., 7.5 hours).

def main():
    time = input("What time is it? ").strip().split(":")
    converted_time = convert(time)
    print(what_meal(converted_time))

def convert(time):
    converted_time = float(int(time[0]) + float(int(time[1])/60))
    return(converted_time)

def what_meal(converted_time):
    if 7.0 <= converted_time <= 8.0:
        return("breakfast")
    if 12.0 <= converted_time <= 13.0:
        return("lunch")
    if 18.0 <= converted_time <= 19.0:
        return("dinner")

if __name__ == "__main__":
     main()