import math

class HINH:
    def nhap(self):
        pass

    def xuat(self):
        pass

    def tinhDienTich(self):
        return 0

    def tinhChuVi(self):
        return 0

class HINHTRON(HINH):
    def __init__(self):
        self.banKinh = 0.0

    def nhap(self):
        self.banKinh = float(input("Nhập bán kính: "))

    def xuat(self):
        print(f"Hình tròn - Bán kính: {self.banKinh} | "
              f"Diện tích: {self.tinhDienTich():.2f} | "
              f"Chu vi: {self.tinhChuVi():.2f}")

    def tinhDienTich(self):
        return math.pi * self.banKinh ** 2

    def tinhChuVi(self):
        return 2 * math.pi * self.banKinh

class HINHCHUNHAT(HINH):
    def __init__(self):
        self.chieuDai = 0.0
        self.chieuRong = 0.0

    def nhap(self):
        self.chieuDai = float(input("Nhập chiều dài: "))
        self.chieuRong = float(input("Nhập chiều rộng: "))

    def xuat(self):
        print(f"Hình chữ nhật - Dài: {self.chieuDai} | "
              f"Rộng: {self.chieuRong} | "
              f"Diện tích: {self.tinhDienTich():.2f} | "
              f"Chu vi: {self.tinhChuVi():.2f}")

    def tinhDienTich(self):
        return self.chieuDai * self.chieuRong

    def tinhChuVi(self):
        return (self.chieuDai + self.chieuRong) * 2

class HINHVUONG(HINH):
    def __init__(self):
        self.canh = 0.0

    def nhap(self):
        self.canh = float(input("Nhập cạnh: "))

    def xuat(self):
        print(f"Hình vuông - Cạnh: {self.canh} | "
              f"Diện tích: {self.tinhDienTich():.2f} | "
              f"Chu vi: {self.tinhChuVi():.2f}")

    def tinhDienTich(self):
        return self.canh ** 2

    def tinhChuVi(self):
        return self.canh * 4

class HINHTAMGIAC(HINH):
    def __init__(self):
        self.a = 0.0
        self.b = 0.0
        self.c = 0.0

    def nhap(self):
        self.a = float(input("Nhập cạnh a: "))
        self.b = float(input("Nhập cạnh b: "))
        self.c = float(input("Nhập cạnh c: "))

    def xuat(self):
        print(f"Hình tam giác - "
              f"a: {self.a}, b: {self.b}, c: {self.c} | "
              f"Diện tích: {self.tinhDienTich():.2f} | "
              f"Chu vi: {self.tinhChuVi():.2f}")

    def tinhChuVi(self):
        return self.a + self.b + self.c

    def tinhDienTich(self):
        p = self.tinhChuVi() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

# Console
dsHinh = []
n = int(input("Nhập số lượng hình: "))
for i in range(n):
    print(f"\nHình thứ {i + 1}")
    print("1. Hình tròn")
    print("2. Hình chữ nhật")
    print("3. Hình vuông")
    print("4. Hình tam giác")
    loai = int(input("Chọn loại hình: "))
    if loai == 1:
        hinh = HINHTRON()
    elif loai == 2:
        hinh = HINHCHUNHAT()
    elif loai == 3:
        hinh = HINHVUONG()
    else:
        hinh = HINHTAMGIAC()
    hinh.nhap()
    dsHinh.append(hinh)

print("\n--- DANH SÁCH HÌNH ---")
for hinh in dsHinh:
    hinh.xuat()
if dsHinh:
    tongDienTich = sum(hinh.tinhDienTich() for hinh in dsHinh)
    maxDienTich = max(hinh.tinhDienTich() for hinh in dsHinh)
    print(f"\nTổng diện tích: {tongDienTich:.2f}")
    print("\n--- HÌNH CÓ DIỆN TÍCH LỚN NHẤT ---")
    for hinh in dsHinh:
        if hinh.tinhDienTich() == maxDienTich:
            hinh.xuat()