class SinhVien:
    def __init__(self):
        self.hoTen = ""
        self.soBaoDanh = ""

    def nhap(self):
        self.hoTen = input("Nhập họ tên: ")
        self.soBaoDanh = input("Nhập số báo danh: ")

    def xuat(self):
        print(f"Họ tên: {self.hoTen} |"
              f" Số báo danh: {self.soBaoDanh}", end=" | ")


class DiemThi(SinhVien):
    def __init__(self):
        super().__init__()
        self.diemMon1 = 0.0
        self.diemMon2 = 0.0

    def nhap(self):
        super().nhap()
        self.diemMon1 = float(input("Nhập điểm môn thi 1: "))
        self.diemMon2 = float(input("Nhập điểm môn thi 2: "))

    def xuat(self):
        super().xuat()
        print(f"Điểm môn 1: {self.diemMon1} |"
              f" Điểm môn 2: {self.diemMon2}", end=" | ")

class KetQua(DiemThi):
    def __init__(self):
        super().__init__()
        self.tongDiem = 0.0

    def tinhTongDiem(self):
        self.tongDiem = self.diemMon1 + self.diemMon2
        return self.tongDiem

    def xuat(self):
        super().xuat()
        print(f"Tổng điểm: {self.tinhTongDiem():.2f}")

# Console
ds = []
n = int(input("Nhập số sinh viên: "))
for i in range(n):
    print(f"\nNhập thông tin sinh viên thứ {i + 1}:")
    sv = KetQua()
    sv.nhap()
    ds.append(sv)

print("\n--- KẾT QUẢ THI ---")
for sv in ds:
    sv.xuat()