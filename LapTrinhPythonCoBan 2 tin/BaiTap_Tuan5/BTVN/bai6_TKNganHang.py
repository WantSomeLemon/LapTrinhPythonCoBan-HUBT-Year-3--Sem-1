class TAIKHOAN:
    def __init__(self):
        self.soTaiKhoan = ""
        self.chuTaiKhoan = ""
        self.soDu = 0.0

    def nhap(self):
        self.soTaiKhoan = input("Nhập số tài khoản: ")
        self.chuTaiKhoan = input("Nhập chủ tài khoản: ")
        self.soDu = float(input("Nhập số dư: "))

    def xuat(self):
        print(f"Số tài khoản: {self.soTaiKhoan} | "
              f"Chủ tài khoản: {self.chuTaiKhoan} | "
              f"Số dư: {self.soDu:,.0f}", end=" | ")

    def tinhLai(self):
        return 0

class TAIKHOANTIETKIEM(TAIKHOAN):
    def __init__(self):
        super().__init__()
        self.kyHan = 0
        self.laiSuat = 0.0

    def nhap(self):
        super().nhap()
        self.kyHan = int(input("Nhập kỳ hạn: "))
        self.laiSuat = float(input("Nhập lãi suất (%): "))

    def tinhLai(self):
        return self.soDu * self.laiSuat / 100 * self.kyHan

    def xuat(self):
        super().xuat()
        print(f"Kỳ hạn: {self.kyHan} | "
              f"Lãi suất: {self.laiSuat}% | "
              f"Tiền lãi: {self.tinhLai():,.0f}")

class TAIKHOANTHANHTOAN(TAIKHOAN):
    def __init__(self):
        super().__init__()
        self.phiDuyTri = 0.0

    def nhap(self):
        super().nhap()
        self.phiDuyTri = float(input("Nhập phí duy trì: "))

    def tinhSoDuThucTe(self):
        return self.soDu - self.phiDuyTri

    def xuat(self):
        super().xuat()
        print(f"Phí duy trì: {self.phiDuyTri:,.0f} | "
              f"Số dư thực tế: {self.tinhSoDuThucTe():,.0f}")

# Console
dsTaiKhoan = []
n = int(input("Nhập số lượng tài khoản: "))
for i in range(n):
    print(f"\nTài khoản thứ {i + 1}")
    print("1. Tài khoản tiết kiệm")
    print("2. Tài khoản thanh toán")
    loai = int(input("Chọn loại tài khoản: "))
    if loai == 1:
        tk = TAIKHOANTIETKIEM()
    else:
        tk = TAIKHOANTHANHTOAN()
    tk.nhap()
    dsTaiKhoan.append(tk)

print("\n--- DANH SÁCH TÀI KHOẢN ---")
for tk in dsTaiKhoan:
    tk.xuat()
if dsTaiKhoan:
    maxSoDu = max(tk.soDu for tk in dsTaiKhoan)
    tongSoDu = sum(tk.soDu for tk in dsTaiKhoan)
    print(f"\nTổng số dư: {tongSoDu:,.0f}")
    print("\n--- TÀI KHOẢN CÓ SỐ DƯ CAO NHẤT ---")
    for tk in dsTaiKhoan:
        if tk.soDu == maxSoDu:
            tk.xuat()
    print("\n--- TIỀN LÃI TÀI KHOẢN TIẾT KIỆM ---")
    for tk in dsTaiKhoan:
        if isinstance(tk, TAIKHOANTIETKIEM):
            print(f"{tk.soTaiKhoan}: {tk.tinhLai():,.0f} VNĐ")