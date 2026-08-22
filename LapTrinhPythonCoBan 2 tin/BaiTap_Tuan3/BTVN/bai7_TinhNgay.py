from datetime import datetime

ngayBatDau = input("Nhập ngày sinh (dd/mm/yyyy): ")
ngayKetThuc = input("Nhập ngày sinh (dd/mm/yyyy): ")
ngayBatDau = datetime.strptime(ngayBatDau, "%d/%m/%Y")
ngayKetThuc = datetime.strptime(ngayKetThuc, "%d/%m/%Y")

while ngayBatDau > ngayKetThuc:
    print("Ngày bắt đầu phải bé hơn ngày kết thúc.")
    ngayBatDau = input("Nhập ngày sinh (dd/mm/yyyy): ")
    ngayKetThuc = input("Nhập ngày sinh (dd/mm/yyyy): ")
    ngayBatDau = datetime.strptime(ngayBatDau, "%d/%m/%Y")
    ngayKetThuc = datetime.strptime(ngayKetThuc, "%d/%m/%Y")

soNgayChenhLech = ngayKetThuc - ngayBatDau
print("Số ngày chênh lệch", soNgayChenhLech.days)
