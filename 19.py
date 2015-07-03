def isLeapYear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False

def daysInMonth(year, month):
    if month in [4, 6, 9, 11]:
        return 30
    if month == 2:
        if isLeapYear(year):
            return 29
        else:
            return 28
    return 31

sundayList = 0
iDay = 1
for year in range(1901, 2001):
    for month in range(1, 13):
        for day in range(1, daysInMonth(year, month)+1):
            iDay += 1
            if day == 1 and iDay%7 == 0:
                sundayList += 1

print(sundayList)
