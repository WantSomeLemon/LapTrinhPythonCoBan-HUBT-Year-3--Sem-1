class sinhVien():
    def __init__(self):
        self.masv=""
        self.ht=""
        self.dtb=0.0
    def nhap(self):
        self.masv=input("Nhập mã sinh viên :")
        self.ht=input("Nhập họ tên sinh viên :")
        self.dtb=float(input("Nhập điểm trung bình :"))
    def hienthi(self):
        print(self.masv,"  ",self.ht,"  ",self.dtb)
listsv=[]
n=int(input("Nhập số sinh viên :"))
for i in range(n):
    sv=sinhVien()
    sv.nhap()
    listsv.append(sv)
for i in listsv:
    i.hienthi()
    
