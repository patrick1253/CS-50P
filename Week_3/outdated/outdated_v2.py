#CS50 assignment:  implement a program that prompts the user 
# for a date, anno Domini, in month-day-year order, formatted 
# like 9/8/1636 or September 8, 1636, wherein the month in the 
# latter might be any of the values in the list below.

# Then output that same date in YYYY-MM-DD format. If the user’s 
# input is not a valid date in either format, prompt the user again. 
# Assume that every month has no more than 31 days; no need to validate 
# whether a month has 28, 29, 30, or 31 days.

def main():
    dateISO = split_date()
    print(dateISO)

months = {    
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12}

def split_date():
    while True:
        status = True
        date = input("Enter a date in MM/DD/YYYY or MONTH DD, YYYY format: ").title()
        date = date.replace(",","")

        # If date is already in MM/DD/YYYY format, break the date into parts
        if date[0].isnumeric():
            splitdate = date.split(sep='/')
            if int(splitdate[0]) > 12:
                print("There are only 12 months")
                status = False

        # If date in MONTH DD, YYYY format, break the date into parts
        else:
            splitdate = date.split(sep=' ')

            # Convert the text month to a number
            if splitdate[0] in months:
                splitdate[0] = str(months[splitdate[0]])
            else:
                print("Please enter the full name of the month")
                status = False

        # Check that no month has more than 31 days (Note: in a more 
        # sophisticated version, this would check max allowable days for 
        # each month indidually.)    
        if int(splitdate[1]) > 31:
            print("Month cannot have more than 31 days")
            status = False

        elif int(splitdate[1]) == 0:
            print("Month cannot have zero days")
            status = False
                 
        if status == True:
            dateISO = (f"{splitdate[2].zfill(4)}-{splitdate[0].zfill(2)}-{splitdate[1].zfill(2)}")
            return dateISO            
        
   
if __name__ == "__main__":
    main()