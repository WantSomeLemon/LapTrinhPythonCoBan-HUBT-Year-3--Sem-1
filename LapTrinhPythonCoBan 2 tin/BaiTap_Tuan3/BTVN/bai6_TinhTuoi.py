from datetime import datetime

today = datetime.now()
ngaysinh = input("Nhập ngày sinh (dd/mm/yyyy): ")
while ngaysinh == "":
    print("Ngày sinh không được rỗng.")
    ngaysinh = input("Nhập ngày sinh (dd/mm/yyyy): ")
dob = datetime.strptime(ngaysinh, "%d/%m/%Y")

while dob > today:
    print("Ngày sinh không được lớn hơn ngày hiện tại.")
    ngaysinh = input("Nhập ngày sinh (dd/mm/yyyy): ")
    dob = datetime.strptime(ngaysinh, "%d/%m/%Y")

tuoi = today.year - dob.year
if (today.month, today.day) < (dob.month, dob.day):
    tuoi -= 1
print("Tuổi:", tuoi)