from datetime import datetime

tenSanPham = input("Nhập tên sản phẩm: ")
ngaySanXuat = input("Nhập ngày sản xuất (dd/mm/yyyy): ")
hanSuDung = input("Nhập hạn sử dụng (dd/mm/yyyy): ")
ngaySanXuat = datetime.strptime(ngaySanXuat, "%d/%m/%Y")
hanSuDung = datetime.strptime(hanSuDung, "%d/%m/%Y")

while hanSuDung < ngaySanXuat:
    print("Hạn sử dụng phải lớn hơn ngày sản xuất.")
    ngaySanXuat = input("Nhập ngày sản xuất (dd/mm/yyyy): ")
    hanSuDung = input("Nhập hạn sử dụng (dd/mm/yyyy): ")
    ngaySanXuat = datetime.strptime(ngaySanXuat, "%d/%m/%Y")
    hanSuDung = datetime.strptime(hanSuDung, "%d/%m/%Y")

today = datetime.now()
print("Tên sản phẩm:", tenSanPham)
if today <= hanSuDung:
    soNgayConLai = hanSuDung - today
    print("Sản phẩm còn hạn.")
    print("Còn", soNgayConLai.days, "ngày.")
else:
    print("Sản phẩm đã hết hạn.")