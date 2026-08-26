from abc import ABC, abstractmethod
import math

class HinhHoc(ABC):
    @abstractmethod
    def tinhDienTich(self):
        pass

    @abstractmethod
    def tinhChuVi(self):
        pass

class HinhTron(HinhHoc):
    def __init__(self, banKinh):
        self.__banKinh = banKinh

    def tinhDienTich(self):
        return math.pi * (self.__banKinh ** 2)

    def tinhChuVi(self):
        return 2 * math.pi * self.__banKinh

class HinhVuong(HinhHoc):
    def __init__(self, canh):
        self.__canh = canh

    def tinhDienTich(self):
        return self.__canh ** 2

    def tinhChuVi(self):
        return self.__canh * 4

class HinhChuNhat(HinhHoc):
    def __init__(self, dai, rong):
        self.__dai = dai
        self.__rong = rong

    def tinhDienTich(self):
        return self.__dai * self.__rong

    def tinhChuVi(self):
        return (self.__dai + self.__rong) * 2

#Console
dsHinh = [
    HinhTron(5),
    HinhVuong(4),
    HinhChuNhat(3, 6)
]

for i, hinh in enumerate(dsHinh, 1):
    print(f"Hình {i} -> Diện tích: {hinh.tinhDienTich():.2f} |"
          f" Chu vi: {hinh.tinhChuVi():.2f}")