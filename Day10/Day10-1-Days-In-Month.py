
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
        

def days_in_month(year, month):
    month_days = [31,28,31,30,31,30,31,31,30,31,20,31]
    
    if is_leap(year):
        if month-1 == 1:
            print("29")
    else:
        print(month_days[month-1])

days_in_month(2022,2)
days_in_month(2000,2)


            