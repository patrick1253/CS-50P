# CS50 assignment: In a file called working.py, implement a function called convert that 
# expects a str in any of the 12-hour formats below and returns the corresponding str in 
# 24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will be capitalized (with no 
# periods therein) and that there will be a space before each. Assume that these times are 
# representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

#    9:00 AM to 5:00 PM
#    9 AM to 5 PM
#    9:00 AM to 5 PM
#    9 AM to 5:00 PM

# Raise a ValueError instead if the input to convert is not in either of those formats or if 
# either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone’s 
# hours will start ante meridiem and end post meridiem; someone might work late and even long h
# ours (e.g., 5:00 PM to 9:00 AM).

import re
import sys

def main():
    print(convert(input("Hours: ")))


def convert(s):

    times = re.search(r"^(.*)\sto\s(.*)$", s)
    start, end = times.groups()

    list = [start, end]
    times = []

    for time in list:
        if matches := re.match(r"^(\d+):*(\d{2})?\s?(AM|PM)?", time):

            if 0 <= int(matches.group(1)) <= 12: 
                hour = matches.group(1)
            else:
                sys.exit("Please express hours as a number between 0 and 12")

                 
            if matches.group(2): 
                if 0 <= int(matches.group(2)) <= 59:
                    min = matches.group(2)
                else:
                    sys.exit("Minutes must be between 0 and 59") 
            else:
                min = "00"   

            if matches.group(3) in ["AM", "PM"]:
                AM_PM = matches.group(3)
                if AM_PM == "PM" and int(hour) < 12:
                    hour = (int(hour) + 12)
                elif AM_PM == "AM" and int(hour) == 12:
                    hour = (int(hour) - 12)
            else:        
                sys.exit("Please indicate AM or PM")            
                
            times.append(f"{hour}:{min}")
    
    result = (" to ".join(times))
    return result


if __name__ == "__main__":
    main()
