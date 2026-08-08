class Person:
    def __init__(self, hoTen="", ngaysinh="", que_quan=""):
        self.hoTen = hoTen
        self.ngaysinh = ngaysinh
        self.que_quan = que_quan

    def nhap(self):
        self.hoTen = input("Họ tên: ")
        self.ngaysinh = input("ngaysinh: ")
        self.que_quan = input("que_quan: ")

    def xuat(self):
        print("Họ tên: ",self.hoTen)
        print("Ngày sinh: ",self.ngaysinh)
        print("Quê quán: ",self.que_quan)



class KySu(Person):
    def __init__(self, ho_ten="", ngay_sinh="", que_quan="",
                 nganh_hoc="", nam_tot_nghiep=0):
        super().__init__(ho_ten, ngay_sinh, que_quan)
        self.nganh_hoc = nganh_hoc
        self.nam_tot_nghiep = nam_tot_nghiep

    def nhap(self):
        super().nhap()
        self.nganh_hoc = input("Ngành học: ")
        self.nam_tot_nghiep = int(input("Năm tốt nghiệp: "))

    def xuat(self):
        super().xuat()
        print("Ngành học:", self.nganh_hoc)
        print("Năm tốt nghiệp:", self.nam_tot_nghiep)