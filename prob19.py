# day counter to 365 for normal, 366 for leap
# year counter from 1901 to 2000
# determine if leap year every time year is changed
# first 31 days of year are January.
# After Jan, skip the rest of the days.
# Determine startiing day of the week.
# Program starts on monday.
# Max of 4 sundays in a January.
# Min of 3 sundays in a January
# Will be max if years starts on Thursday, Friday, Saturday, or Sunday
# Will be min if years starts on Wednesday, Tuesday, or Monday
# If normal year, the starting day of Jan increases by one.
# Ie. Monday->Tuesday or Friday->Saturday
# If leap year, the starting day of Jan increase by two.
# Ie. Monday->Wednesday or Friday->Sunday

def main():
    numSunday = 0
    numLeap = 0
    currDay = 1 #Monday == 1, Tuesday == 2, ..., Sunday == 7
    startYear = int(input("Please enter the starting year: "))
    endYear = int(input("Please enter the ending year: "))

    while(startYear != endYear+1):

        
        # Counts Sundays in current year
        if currDay == 7:
            numSunday += 1
        
        # Checks for leap Year
        if (startYear % 4 == 0):
            currDay += 2
            numLeap += 1
        else:
            currDay += 1

        # Loops week over if day is greater than 7
        if currDay > 7:
            currDay = currDay % 7

        # Increments year
        startYear += 1
        print(currDay)
        
    print("There are", numSunday ,"sundays")
    print(numLeap)
main()
