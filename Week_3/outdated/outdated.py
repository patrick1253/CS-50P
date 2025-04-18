#CS50 assignment:  implement a program that prompts the user 
# for a date, anno Domini, in month-day-year order, formatted 
# like 9/8/1636 or September 8, 1636, wherein the month in the 
# latter might be any of the values in the list below.

# Then output that same date in YYYY-MM-DD format. If the user’s 
# input is not a valid date in either format, prompt the user again. 
# Assume that every month has no more than 31 days; no need to validate 
# whether a month has 28, 29, 30, or 31 days.

def main():
    #date = input("Enter a date in MM/DD/YYYY or MONTH DD, YYYY format: ")
    ISOdate = convert_MEdate()
    print(ISOdate)

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

# Converts MONTH DD, YYYY format to MM/DD/YYYY format

def make_MEdate():
    while True:
        date = input("Enter a date in MM/DD/YYYY or MONTH DD, YYYY format: ")

        if date[0].isnumeric():
            MEdate = date
            return MEdate
        else:
            date = date.split(sep=' ')

        if date[0] in months:
            date[0] = months[date[0]]
            date[1] = date[1][:-1]
        else:
            return
        
        if int(date[1]) < 31:
            MEdate = (f"{date[0]}/{date[1]}/{date[2]}")
            return(MEdate)
        else:
            return
    
def convert_MEdate():
    MEdate = make_MEdate()
    MEdate = MEdate.split(sep='/')
    
    # To just change oder in which columns are printed
    ISOdate = (f"{MEdate[2].zfill(4)}-{MEdate[0].zfill(2)}-{MEdate[1].zfill(2)}")
    return ISOdate

    # To reorder columns:
    #temp = MEdate[0]
    #MEdate[0] = MEdate[2]
    #MEdate[2] = MEdate[1]
    #MEdate[1] = temp

if __name__ == "__main__":
    main()