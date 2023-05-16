def is_leap(year):
    if year % 4 ==0:
        if year % 100==0:
            if year %400==0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
def days_of_month(year,month):
    """This is a document for my Project
    This is for test"""
    month_days=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year)==True and month==2:
        print(f"Days of the month is 29")
    else:
        print(f"Days of the month is {month_days[month-1]}")
print(days_of_month(2001,2))
