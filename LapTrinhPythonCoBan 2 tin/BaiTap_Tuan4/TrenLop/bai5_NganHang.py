class Account:
    LAISUAT = 0.035

    def __init__(self, soTK, tenChuTK, soTien=50.0):
        self.soTK = soTK
        self.tenChuTK = tenChuTK
        self.soTien = soTien

    def inThongTin(self):
        print(f"Số TK: {self.soTK} |"
              f" Chủ TK: {self.tenChuTK} |"
              f" Số dư: {self.soTien:,.2f}")

    def napTien(self, soTienNap):
        if soTienNap > 0:
            self.soTien += soTienNap
            print("Nạp tiền thành công!")
        else:
            print("Số tiền nạp không hợp lệ!")

    def rutTien(self, soTienRut, phiRut=0.33):
        tongTru = soTienRut + phiRut
        if 0 < tongTru <= self.soTien:
            self.soTien -= tongTru
            print("Rút tiền thành công!")
        else:
            print("Số tiền rút vượt quá số dư hoặc không hợp lệ!")

    def daoHan(self):
        self.soTien += self.soTien * Account.LAISUAT
        print("Đã đáo hạn thành công!")

    def chuyenKhoan(self, tk_nhan, soTienChuyen):
        if 0 < soTienChuyen <= self.soTien:
            self.soTien -= soTienChuyen
            tk_nhan.soTien += soTienChuyen
            print("Chuyển khoản thành công!")
        else:
            print("Chuyển khoản thất bại!")

#Console
tk1 = Account("12345", "Nguyen Van A", 1000.0)
tk2 = Account("67890", "Tran Thi B") # Mặc định 50.0

print("Thông tin ban đầu:")
tk1.inThongTin()
tk2.inThongTin()
print("\nThực hiện giao dịch:")
tk1.napTien(500)
tk1.rutTien(200)
tk1.daoHan()
tk1.chuyenKhoan(tk2, 300)
print("\nThông tin sau giao dịch:")
tk1.inThongTin()
tk2.inThongTin()