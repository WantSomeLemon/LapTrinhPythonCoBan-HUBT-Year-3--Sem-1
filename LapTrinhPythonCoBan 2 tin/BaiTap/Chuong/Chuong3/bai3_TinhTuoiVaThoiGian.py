from datetime import datetime

ngaysinh = input("Nhập ngày sinh (dd/mm/yyyy): ")

dob = datetime.strptime(ngaysinh, "%d/%m/%Y")
today = datetime.now()

tuoi = today.year - dob.year

if (today.month, today.day) < (dob.month, dob.day):
    tuoi -= 1

print("Tuổi:", tuoi)

songay = (today - dob).days

print("Số ngày đã trôi qua:", songay)

print("Ngày hiện tại:", today.strftime("%d/%m/%Y"))
print("Giờ hiện tại:", today.strftime("%H:%M:%S"))