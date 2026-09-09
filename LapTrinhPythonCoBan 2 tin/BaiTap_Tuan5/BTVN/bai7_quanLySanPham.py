from datetime import datetime

class SANPHAM:
    def __init__(self):
        self.ma = ""
        self.ten = ""
        self.gia = 0.0
        self.soLuong = 0

    def nhap(self):
        self.ma = input("Nhập mã sản phẩm: ")
        self.ten = input("Nhập tên sản phẩm: ")
        self.gia = float(input("Nhập giá: "))
        self.soLuong = int(input("Nhập số lượng: "))

    def xuat(self):
        print(f"Mã: {self.ma} | "
              f"Tên: {self.ten} | "
              f"Giá: {self.gia:,.0f} | "
              f"Số lượng: {self.soLuong}", end=" | ")

    def tinhThanhTien(self):
        return self.gia * self.soLuong

class DIENTU(SANPHAM):
    def __init__(self):
        super().__init__()
        self.thoiGianBaoHanh = 0
        self.phiBaoHanh = 0.0

    def nhap(self):
        super().nhap()
        self.thoiGianBaoHanh = int(input("Nhập thời gian bảo hành: "))
        self.phiBaoHanh = float(input("Nhập phí bảo hành: "))

    def xuat(self):
        super().xuat()
        print(f"Thời gian bảo hành: {self.thoiGianBaoHanh} | "
              f"Phí bảo hành: {self.phiBaoHanh:,.0f} | "
              f"Thành tiền: {self.tinhThanhTien():,.0f}")

class THUCPHAM(SANPHAM):
    def __init__(self):
        super().__init__()
        self.ngaySanXuat = ""
        self.ngayHetHan = ""

    def nhap(self):
        super().nhap()
        self.ngaySanXuat = input("Nhập ngày sản xuất (dd/mm/yyyy): ")
        self.ngayHetHan = input("Nhập ngày hết hạn (dd/mm/yyyy): ")

    def daHetHan(self):
        ngayHetHan = datetime.strptime(self.ngayHetHan, "%d/%m/%Y")
        return ngayHetHan < datetime.now()

    def xuat(self):
        super().xuat()
        print(f"Ngày sản xuất: {self.ngaySanXuat} | "
              f"Ngày hết hạn: {self.ngayHetHan} | "
              f"Thành tiền: {self.tinhThanhTien():,.0f}")

# Console
dsSanPham = []
n = int(input("Nhập số lượng sản phẩm: "))
for i in range(n):
    print(f"\nSản phẩm thứ {i + 1}")
    print("1. Điện tử")
    print("2. Thực phẩm")
    loai = int(input("Chọn loại: "))
    if loai == 1:
        sp = DIENTU()
    else:
        sp = THUCPHAM()
    sp.nhap()
    dsSanPham.append(sp)
print("\n--- DANH SÁCH SẢN PHẨM ---")
for sp in dsSanPham:
    sp.xuat()
if dsSanPham:
    maxThanhTien = max(sp.tinhThanhTien() for sp in dsSanPham)
    tongTonKho = sum(sp.tinhThanhTien() for sp in dsSanPham)
    print(f"\nTổng giá trị tồn kho: {tongTonKho:,.0f}")
    print("\n--- SẢN PHẨM CÓ GIÁ TRỊ CAO NHẤT ---")
    for sp in dsSanPham:
        if sp.tinhThanhTien() == maxThanhTien:
            sp.xuat()
            
    print("\n--- THỰC PHẨM ĐÃ HẾT HẠN ---")
    for sp in dsSanPham:
        if isinstance(sp, THUCPHAM) and sp.daHetHan():
            sp.xuat()