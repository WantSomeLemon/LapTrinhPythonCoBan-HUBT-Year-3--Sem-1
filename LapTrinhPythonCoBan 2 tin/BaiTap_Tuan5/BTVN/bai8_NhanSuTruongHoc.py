class NHANSU:
    def __init__(self):
        self.ma = ""
        self.hoTen = ""
        self.ngaySinh = ""
        self.diaChi = ""

    def nhap(self):
        self.ma = input("Nhập mã: ")
        self.hoTen = input("Nhập họ tên: ")
        self.ngaySinh = input("Nhập ngày sinh: ")
        self.diaChi = input("Nhập địa chỉ: ")

    def xuat(self):
        print(f"Mã: {self.ma} | "
              f"Họ tên: {self.hoTen} | "
              f"Ngày sinh: {self.ngaySinh} | "
              f"Địa chỉ: {self.diaChi}", end=" | ")

    def tinhLuong(self):
        return 0

class GIANGVIEN(NHANSU):
    def __init__(self):
        super().__init__()
        self.boMon = ""
        self.soTiet = 0
        self.tienMotTiet = 0.0

    def nhap(self):
        super().nhap()
        self.boMon = input("Nhập bộ môn: ")
        self.soTiet = int(input("Nhập số tiết dạy: "))
        self.tienMotTiet = float(input("Nhập tiền mỗi tiết: "))

    def tinhLuong(self):
        return self.soTiet * self.tienMotTiet

    def xuat(self):
        super().xuat()
        print(f"Bộ môn: {self.boMon} | "
              f"Số tiết: {self.soTiet} | "
              f"Tiền mỗi tiết: {self.tienMotTiet:,.0f} | "
              f"Lương: {self.tinhLuong():,.0f}")

class NHANVIEN(NHANSU):
    def __init__(self):
        super().__init__()
        self.boPhan = ""
        self.heSoLuong = 0.0
        self.luongCoBan = 0.0

    def nhap(self):
        super().nhap()
        self.boPhan = input("Nhập bộ phận: ")
        self.heSoLuong = float(input("Nhập hệ số lương: "))
        self.luongCoBan = float(input("Nhập lương cơ bản: "))

    def tinhLuong(self):
        return self.heSoLuong * self.luongCoBan

    def xuat(self):
        super().xuat()
        print(f"Bộ phận: {self.boPhan} | "
              f"Hệ số lương: {self.heSoLuong} | "
              f"Lương cơ bản: {self.luongCoBan:,.0f} | "
              f"Lương: {self.tinhLuong():,.0f}")

# Console
dsNhanSu = []
n = int(input("Nhập số lượng nhân sự: "))
for i in range(n):
    print(f"\nNhân sự thứ {i + 1}")
    print("1. Giảng viên")
    print("2. Nhân viên")
    loai = int(input("Chọn loại: "))
    if loai == 1:
        ns = GIANGVIEN()
    else:
        ns = NHANVIEN()
    ns.nhap()
    dsNhanSu.append(ns)

print("\n--- DANH SÁCH NHÂN SỰ ---")
for ns in dsNhanSu:
    ns.xuat()
if dsNhanSu:
    tongLuong = sum(ns.tinhLuong() for ns in dsNhanSu)
    maxLuong = max(ns.tinhLuong() for ns in dsNhanSu)
    print(f"\nTổng tiền lương: {tongLuong:,.0f}")
    print("\n--- NHÂN SỰ CÓ LƯƠNG CAO NHẤT ---")
    for ns in dsNhanSu:
        if ns.tinhLuong() == maxLuong:
            ns.xuat()
    soGiangVien = 0
    soNhanVien = 0

    for ns in dsNhanSu:
        if isinstance(ns, GIANGVIEN):
            soGiangVien += 1
        elif isinstance(ns, NHANVIEN):
            soNhanVien += 1
    print(f"\nSố giảng viên: {soGiangVien}")
    print(f"Số nhân viên: {soNhanVien}")