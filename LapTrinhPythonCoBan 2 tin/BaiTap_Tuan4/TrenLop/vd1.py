class sinhVien:
    masv=""
    ht=""
    tuoi=""
    dc=""
    def hienthi(self):
        print("Mã sinh viên :",self.masv)
        print("Họ tên sinh viên :",self.ht)
        print("Tuổi sinh viên:",self.tuoi)
        print("Địa chỉ sinh viên:",self.dc)
    def add(self):
        self.masv=input("Nhập mã sinh viên :")
        self.ht=input("Nhập họ tên sinh viên :")
        self.tuoi=input("Nhập tuổi sinh viên :")
        self.dc=input("Nhập địa chỉ sinh viên")

sv=sinhVien()
sv.add()
sv.hienthi()
