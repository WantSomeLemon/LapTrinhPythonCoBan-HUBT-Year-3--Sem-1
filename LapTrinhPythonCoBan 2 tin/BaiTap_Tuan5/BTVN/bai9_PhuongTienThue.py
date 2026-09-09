class XE:
    def __init__(self):
        self.ma = ""
        self.ten = ""
        self.hangSanXuat = ""
        self.giaThueNgay = 0.0

    def nhap(self):
        self.ma = input("Nhập mã xe: ")
        self.ten = input("Nhập tên xe: ")
        self.hangSanXuat = input("Nhập hãng sản xuất: ")
        self.giaThueNgay = float(input("Nhập giá thuê/ngày: "))

    def xuat(self):
        print(f"Mã: {self.ma} | "
              f"Tên: {self.ten} | "
              f"Hãng SX: {self.hangSanXuat} | "
              f"Giá thuê/ngày: {self.giaThueNgay:,.0f}", end=" | ")

    def tinhTienThue(self):
        return 0

class OTO(XE):
    def __init__(self):
        super().__init__()
        self.soCho = 0
        self.soNgay = 0

    def nhap(self):
        super().nhap()
        self.soCho = int(input("Nhập số chỗ: "))
        self.soNgay = int(input("Nhập số ngày thuê: "))

    def tinhTienThue(self):
        tien = self.giaThueNgay * self.soNgay

        if self.soNgay > 7:
            tien = tien * 90 / 100

        return tien

    def xuat(self):
        super().xuat()
        print(f"Số chỗ: {self.soCho} | "
              f"Số ngày thuê: {self.soNgay} | "
              f"Tiền thuê: {self.tinhTienThue():,.0f}")

class XEMAY(XE):
    def __init__(self):
        super().__init__()
        self.dungTichXiLanh = 0.0
        self.soNgay = 0

    def nhap(self):
        super().nhap()
        self.dungTichXiLanh = float(input("Nhập dung tích xi-lanh: "))
        self.soNgay = int(input("Nhập số ngày thuê: "))

    def tinhTienThue(self):
        tien = self.giaThueNgay * self.soNgay
        if self.soNgay > 7:
            tien = tien * 90 / 100
        return tien

    def xuat(self):
        super().xuat()
        print(f"Dung tích xi-lanh: {self.dungTichXiLanh} | "
              f"Số ngày thuê: {self.soNgay} | "
              f"Tiền thuê: {self.tinhTienThue():,.0f}")

# Console
dsXe = []
n = int(input("Nhập số lượng xe: "))
for i in range(n):
    print(f"\nXe thứ {i + 1}")
    print("1. Ô tô")
    print("2. Xe máy")
    loai = int(input("Chọn loại xe: "))
    if loai == 1:
        xe = OTO()
    else:
        xe = XEMAY()
    xe.nhap()
    dsXe.append(xe)

print("\n--- DANH SÁCH XE ---")
for xe in dsXe:
    xe.xuat()
if dsXe:
    tongTien = sum(xe.tinhTienThue() for xe in dsXe)
    maxTien = max(xe.tinhTienThue() for xe in dsXe)
    print(f"\nTổng doanh thu: {tongTien:,.0f}")
    print("\n--- HỢP ĐỒNG CÓ TIỀN THUÊ CAO NHẤT ---")
    for xe in dsXe:
        if xe.tinhTienThue() == maxTien:
            xe.xuat()

    print("\n--- XE THUÊ TRÊN 7 NGÀY ---")
    for xe in dsXe:
        if xe.soNgay > 7:
            xe.xuat()