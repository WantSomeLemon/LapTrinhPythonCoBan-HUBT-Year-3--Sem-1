class PHUONGTIEN:
    def __init__(self):
        self.bienSo = ""
        self.hangSanXuat = ""
        self.namSanXuat = 0
        self.gia = 0.0

    def nhap(self):
        self.bienSo = input("Nhập biển số: ")
        self.hangSanXuat = input("Nhập hãng sản xuất: ")
        self.namSanXuat = int(input("Nhập năm sản xuất: "))
        self.gia = float(input("Nhập giá: "))

    def xuat(self):
        print(f"Biển số: {self.bienSo} | "
              f"Hãng: {self.hangSanXuat} | "
              f"Năm SX: {self.namSanXuat} | "
              f"Giá: {self.gia:,.0f}", end=" | ")

    def tinhThue(self):
        return 0

class OTO(PHUONGTIEN):
    def __init__(self):
        super().__init__()
        self.soCho = 0
        self.dungTichDongCo = 0.0

    def nhap(self):
        super().nhap()
        self.soCho = int(input("Nhập số chỗ: "))
        self.dungTichDongCo = float(input("Nhập dung tích động cơ: "))

    def tinhThue(self):
        return self.gia * 10 / 100

    def xuat(self):
        super().xuat()
        print(f"Số chỗ: {self.soCho} | "
              f"Dung tích động cơ: {self.dungTichDongCo} | "
              f"Thuế: {self.tinhThue():,.0f} | "
              f"Giá sau thuế: {self.gia + self.tinhThue():,.0f}")

class XEMAY(PHUONGTIEN):
    def __init__(self):
        super().__init__()
        self.dungTichXiLanh = 0.0

    def nhap(self):
        super().nhap()
        self.dungTichXiLanh = float(input("Nhập dung tích xi-lanh: "))

    def tinhThue(self):
        return self.gia * 5 / 100

    def xuat(self):
        super().xuat()
        print(f"Dung tích xi-lanh: {self.dungTichXiLanh} | "
              f"Thuế: {self.tinhThue():,.0f} | "
              f"Giá sau thuế: {self.gia + self.tinhThue():,.0f}")

# Console
dsPhuongTien = []
n = int(input("Nhập số lượng phương tiện: "))
for i in range(n):
    print(f"\nPhương tiện thứ {i + 1}")
    print("1. Ô tô")
    print("2. Xe máy")
    loai = int(input("Chọn loại: "))
    if loai == 1:
        pt = OTO()
    else:
        pt = XEMAY()
    pt.nhap()
    dsPhuongTien.append(pt)

print("\n--- DANH SÁCH PHƯƠNG TIỆN ---")
for pt in dsPhuongTien:
    pt.xuat()

if dsPhuongTien:
    tongThue = sum(pt.tinhThue() for pt in dsPhuongTien)
    print(f"\nTổng tiền thuế: {tongThue:,.0f}")
    oto = [pt for pt in dsPhuongTien if isinstance(pt, OTO)]
    xeMay = [pt for pt in dsPhuongTien if isinstance(pt, XEMAY)]
    if oto:
        maxGiaOto = max(pt.gia for pt in oto)
        print("\n--- Ô TÔ CÓ GIÁ CAO NHẤT ---")
        for pt in oto:
            if pt.gia == maxGiaOto:
                pt.xuat()
    if xeMay:
        maxXiLanh = max(pt.dungTichXiLanh for pt in xeMay)
        print("\n--- XE MÁY CÓ DUNG TÍCH XI-LANH LỚN NHẤT ---")
        for pt in xeMay:
            if pt.dungTichXiLanh == maxXiLanh:
                pt.xuat()