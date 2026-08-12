month = int(input("Nhập tháng: "))


if month in [1,3,5,7,8,10,12]:
    days = 31
elif month in [4,6,9,11]:
    days = 30
elif month == 2:
    year = int(input("Nhập năm: "))
    if(year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        days = 29
    else:
        days = 28
else:
    days = 0

if days == 0:
    print("Tháng hoặc Năm không hợp lệ")
else:
    print("Tháng ", month, " có: ", days, " ngày")