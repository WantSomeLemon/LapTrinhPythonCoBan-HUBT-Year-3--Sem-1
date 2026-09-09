class NHANVIEN:
    def __init__(self):
        self.ma = ""
        self.hoTen = ""
        self.ngaySinh = ""
        self.luongCoBan = 0.0

    def nhap(self):
        self.ma = input("Nhập mã nhân viên: ")
        self.hoTen = input("Nhập họ tên: ")
        self.ngaySinh = input("Nhập ngày sinh: ")
        self.luongCoBan = float(input("Nhập lương cơ bản: "))

    def xuat(self):
        print(f"Mã: {self.ma} | "
              f"Họ tên: {self.hoTen} | "
              f"Ngày sinh: {self.ngaySinh} | "
              f"Lương cơ bản: {self.luongCoBan:,.0f}", end=" | ")

    def tinhLuong(self):
        return self.luongCoBan

class NHANVIEN_VANPHONG(NHANVIEN):
    def __init__(self):
        super().__init__()
        self.soNgayCong = 0
        self.phuCap = 0.0

    def nhap(self):
        super().nhap()
        self.soNgayCong = int(input("Nhập số ngày công: "))
        self.phuCap = float(input("Nhập phụ cấp: "))

    def tinhLuong(self):
        return self.luongCoBan + self.soNgayCong * 200000 + self.phuCap

    def xuat(self):
        super().xuat()
        print(f"Số ngày công: {self.soNgayCong} | "
              f"Phụ cấp: {self.phuCap:,.0f} | "
              f"Lương: {self.tinhLuong():,.0f}")

class NHANVIEN_KINHDOANH(NHANVIEN):
    def __init__(self):
        super().__init__()
        self.doanhSo = 0.0
        self.tyLeHoaHong = 0.0

    def nhap(self):
        super().nhap()
        self.doanhSo = float(input("Nhập doanh số: "))
        self.tyLeHoaHong = float(input("Nhập tỷ lệ hoa hồng (%): "))

    def tinhLuong(self):
        return self.luongCoBan + self.doanhSo * self.tyLeHoaHong / 100

    def xuat(self):
        super().xuat()
        print(f"Doanh số: {self.doanhSo:,.0f} | "
              f"Tỷ lệ hoa hồng: {self.tyLeHoaHong}% | "
              f"Lương: {self.tinhLuong():,.0f}")

# Console
dsNhanVien = []
n = int(input("Nhập số lượng nhân viên: "))
for i in range(n):
    print(f"\nNhân viên thứ {i + 1}")
    print("1. Nhân viên văn phòng")
    print("2. Nhân viên kinh doanh")
    loai = int(input("Chọn loại nhân viên: "))
    if loai == 1:
        nv = NHANVIEN_VANPHONG()
    else:
        nv = NHANVIEN_KINHDOANH()
    nv.nhap()
    dsNhanVien.append(nv)

print("\n--- DANH SÁCH NHÂN VIÊN ---")
for nv in dsNhanVien:
    nv.xuat()

if dsNhanVien:
    tongLuong = sum(nv.tinhLuong() for nv in dsNhanVien)
    maxLuong = max(nv.tinhLuong() for nv in dsNhanVien)
    print(f"\nTổng tiền lương: {tongLuong:,.0f}")
    print("\n--- NHÂN VIÊN CÓ LƯƠNG CAO NHẤT ---")
    for nv in dsNhanVien:
        if nv.tinhLuong() == maxLuong:
            nv.xuat()
    soVanPhong = 0
    soKinhDoanh = 0
    for nv in dsNhanVien:
        if isinstance(nv, NHANVIEN_VANPHONG):
            soVanPhong += 1
        elif isinstance(nv, NHANVIEN_KINHDOANH):
            soKinhDoanh += 1
    print(f"\nSố nhân viên văn phòng: {soVanPhong}")
    print(f"Số nhân viên kinh doanh: {soKinhDoanh}")