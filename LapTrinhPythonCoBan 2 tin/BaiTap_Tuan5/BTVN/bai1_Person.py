class Person:
    def __init__(self):
        self.hoTen = ""
        self.ngaySinh = ""
        self.queQuan = ""

    def nhap(self):
        self.hoTen = input("Nhập họ tên: ")
        self.ngaySinh = input("Nhập ngày sinh: ")
        self.queQuan = input("Nhập quê quán: ")

    def xuat(self):
        print(f"Họ tên: {self.hoTen} |"
              f" Ngày sinh: {self.ngaySinh} |"
              f" Quê quán: {self.queQuan}", end=" | ")

class KySu(Person):
    def __init__(self):
        super().__init__()
        self.nganhHoc = ""
        self.namTotNghiep = 0

    def nhap(self):
        super().nhap()
        self.nganhHoc = input("Nhập ngành học: ")
        self.namTotNghiep = int(input("Nhập năm tốt nghiệp: "))

    def xuat(self):
        super().xuat()
        print(f"Ngành học: {self.nganhHoc} |"
              f" Năm tốt nghiệp: {self.namTotNghiep}")

# Console
dsKySu = []
n = int(input("Nhập số lượng kỹ sư: "))
for i in range(n):
    print(f"\nNhập thông tin kỹ sư thứ {i + 1}:")
    ks = KySu()
    ks.nhap()
    dsKySu.append(ks)

print("\n--- DANH SÁCH KỸ SƯ ---")
for ks in dsKySu:
    ks.xuat()

maxNam = max(ks.namTotNghiep for ks in dsKySu)
print(f"\n--- KỸ SƯ TỐT NGHIỆP GẦN ĐÂY NHẤT ({maxNam}) ---")
for ks in dsKySu:
    if ks.namTotNghiep == maxNam:
        ks.xuat()