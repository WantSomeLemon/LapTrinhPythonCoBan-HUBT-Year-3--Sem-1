class NHANVIEN:
    def __init__(self):
        self.ten = ""
        self.tuoi = 0
        self.diachi = ""
        self.luong = 0
        self.giolam = 0

    def inputInfo(self):
        self.ten = input("Nhập tên: ")
        self.tuoi = int(input("Nhập tuổi: "))
        self.diachi = input("Nhập địa chỉ: ")
        self.luong = float(input("Nhập lương: "))
        self.giolam = int(input("Nhập số giờ làm: "))

    def tinhThuong(self):
        if self.giolam > 200:
            return self.luong * 0.2
        elif self.giolam > 100:
            return self.luong * 0.1
        else:
            return 0

    def printInfo(self):
        print("\n===== THÔNG TIN NHÂN VIÊN =====")
        print("Tên:", self.ten)
        print("Tuổi:", self.tuoi)
        print("Địa chỉ:", self.diachi)
        print("Lương:", self.luong)
        print("Giờ làm:", self.giolam)
        print("Thưởng:", self.tinhThuong())

# Console
nv = NHANVIEN()
nv.inputInfo()
nv.printInfo()