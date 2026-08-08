class SinhVien:
    def __init__(self, ho_ten="", so_bao_danh=""):
        self.ho_ten = ho_ten
        self.so_bao_danh = so_bao_danh

    def nhap(self):
        self.ho_ten = input("Họ và tên: ")
        self.so_bao_danh = input("Số báo danh: ")

    def xuat(self):
        print("Họ và tên:", self.ho_ten)
        print("Số báo danh:", self.so_bao_danh)


class DiemThi(SinhVien):
    def __init__(self, ho_ten="", so_bao_danh="",
                 diem_mon_1=0, diem_mon_2=0):
        super().__init__(ho_ten, so_bao_danh)
        self.diem_mon_1 = diem_mon_1
        self.diem_mon_2 = diem_mon_2

    def nhap(self):
        super().nhap()

        self.diem_mon_1 = float(input("Điểm môn 1: "))
        self.diem_mon_2 = float(input("Điểm môn 2: "))

    def xuat(self):
        super().xuat()
        print("Điểm môn 1:", self.diem_mon_1)
        print("Điểm môn 2:", self.diem_mon_2)


class KetQua(DiemThi):
    def __init__(self, ho_ten="", so_bao_danh="",
                 diem_mon_1=0, diem_mon_2=0):
        super().__init__(
            ho_ten,
            so_bao_danh,
            diem_mon_1,
            diem_mon_2
        )

        self.tong_diem = 0

    def tinh_tong_diem(self):
        self.tong_diem = self.diem_mon_1 + self.diem_mon_2

    def nhap(self):
        super().nhap()
        self.tinh_tong_diem()

    def xuat(self):
        super().xuat()
        print("Tổng điểm:", self.tong_diem)