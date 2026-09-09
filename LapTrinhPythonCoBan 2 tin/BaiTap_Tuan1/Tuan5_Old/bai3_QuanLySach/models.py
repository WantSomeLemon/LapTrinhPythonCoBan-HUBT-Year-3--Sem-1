class SACH:
    def __init__(self, ten_sach="", tac_gia="", gia_ban=0):
        self.ten_sach = ten_sach
        self.tac_gia = tac_gia
        self.gia_ban = gia_ban

    def nhap(self):
        self.ten_sach = input("Tên sách: ")
        self.tac_gia = input("Tác giả: ")
        self.gia_ban = float(input("Giá bán: "))

    def xuat(self):
        print("Tên sách:", self.ten_sach)
        print("Tác giả:", self.tac_gia)
        print("Giá bán:", self.gia_ban)


class BIA(SACH):
    def __init__(self, ten_sach="", tac_gia="", gia_ban=0,
                 ma_hinh_anh="", tien_ve=0):
        super().__init__(ten_sach, tac_gia, gia_ban)
        self.ma_hinh_anh = ma_hinh_anh
        self.tien_ve = tien_ve

    def nhap(self):
        super().nhap()

        self.ma_hinh_anh = input("Mã hình ảnh: ")
        self.tien_ve = float(input("Tiền vẽ: "))

    def xuat(self):
        super().xuat()
        print("Mã hình ảnh:", self.ma_hinh_anh)
        print("Tiền vẽ:", self.tien_ve)


class HOASY:
    def __init__(self, ho_ten="", dia_chi=""):
        self.ho_ten = ho_ten
        self.dia_chi = dia_chi

    def nhap(self):
        self.ho_ten = input("Họ tên họa sĩ: ")
        self.dia_chi = input("Địa chỉ họa sĩ: ")

    def xuat(self):
        print("Họ tên họa sĩ:", self.ho_ten)
        print("Địa chỉ họa sĩ:", self.dia_chi)


class SACHVEBIA(BIA, HOASY):
    def __init__(self, ten_sach="", tac_gia="", gia_ban=0,
                 ma_hinh_anh="", tien_ve=0,
                 ho_ten="", dia_chi=""):

        BIA.__init__(
            self,
            ten_sach,
            tac_gia,
            gia_ban,
            ma_hinh_anh,
            tien_ve
        )

        HOASY.__init__(
            self,
            ho_ten,
            dia_chi
        )

        self.tong_tien = 0

    def nhap(self):
        BIA.nhap(self)
        HOASY.nhap(self)

        self.tinh_tong_tien()

    def tinh_tong_tien(self):
        self.tong_tien = self.gia_ban + self.tien_ve

    def xuat(self):
        BIA.xuat(self)
        HOASY.xuat(self)

        print("Tổng tiền:", self.tong_tien)