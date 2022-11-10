year=int(input("year= "))
month=int(input("month= "))
day=int(input("day= "))
print("max dayes can added is 1001")
add=int(input("needed days= "))
arr=[31,29,31,30,31,30,31,31,30,31,30,31]
def check_if_leap(year):
    if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
       arr[1]  = 29
    else:
        arr[1]= 28
    return arr

def addDayes (year,month,day,add):
        check_if_leap(year)
        x = day + add
        if add>0:
            while x> arr[month-1]:
                month+=1
                if month>12:
                    month+=1
                    year+=1
                check_if_leap(year)
                x -= arr[month - 1]

        else:
                while x <= 0:
                    month -= 1
                    if month <= 0:
                        month = 12
                        year -= 1
                    check_if_leap(year)
                    x += arr[month - 1]
        day = x
        print(f"{year}/{month}/{day}")
if (month >= 1 and month <= 12) and (year >= 1999 and year <= 2022) and (day <= arr[
        month - 1] )and (abs(add) < 1001 and abs(add) > 0):
    addDayes(year,month,day,add)
else:
    print("invalid input")


