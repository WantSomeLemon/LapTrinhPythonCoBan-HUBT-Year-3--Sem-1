class Nguoi:
    def __init__(self, hoTen="", tuoi=0):
        self.hoTen = hoTen
        self.tuoi = tuoi

    def hienThi(self):
        print(f"Họ tên: {self.hoTen} |"
              f" Tuổi: {self.tuoi}", end=" ")

class SinhVien(Nguoi):
    def __init__(self, hoTen="", tuoi=0, mssv="",
                 diemToan=0.0, diemVan=0.0):
        super().__init__(hoTen, tuoi)
        self.mssv = mssv
        self.diemToan = diemToan
        self.diemVan = diemVan

    def tinhDTB(self):
        return (self.diemToan + self.diemVan) / 2

    def xepLoai(self):
        dtb = self.tinhDTB()
        if dtb >= 8.0:
            return "Giỏi"
        elif dtb >= 6.5:
            return "Khá"
        elif dtb >= 5.0:
            return "Trung bình"
        else:
            return "Yếu"

    def hienThi(self):
        super().hienThi()
        print(f"| MSSV: {self.mssv} |"
              f" Toán: {self.diemToan} |"
              f" Văn: {self.diemVan} |"
              f" ĐTB: {self.tinhDTB():.2f} |"
              f" Xếp loại: {self.xepLoai()}")

class LopHoc:
    def __init__(self):
        self.dsSV = []

    def themSV(self, sv):
        self.dsSV.append(sv)
        print("Đã thêm sinh viên thành công!")

    def hienThiDanhSach(self):
        print("\n--- DANH SÁCH SINH VIÊN TRONG LỚP ---")
        if not self.dsSV:
            print("Danh sách trống!")
        for sv in self.dsSV:
            sv.hienThi()

    def timSV(self, mssv):
        for sv in self.dsSV:
            if sv.mssv == mssv:
                return sv
        return None

    def xoaSV(self, mssv):
        sv = self.timSV(mssv)
        if sv:
            self.dsSV.remove(sv)
            print(f"Đã xóa sinh viên có MSSV: {mssv}")
        else:
            print("Không tìm thấy sinh viên cần xóa!")

# Console
lopHoc = LopHoc()

lopHoc.themSV(SinhVien("Nguyen Van An", 20, "SV01", 8.5, 9.0))
lopHoc.themSV(SinhVien("Tran Thi Binh", 19, "SV02", 6.0, 7.0))

lopHoc.hienThiDanhSach()

print("\nTìm kiếm sinh viên SV01:")
kq = lopHoc.timSV("SV01")
if kq:
    kq.hienThi()

print("\nXóa sinh viên SV02:")
lopHoc.xoaSV("SV02")

lopHoc.hienThiDanhSach()