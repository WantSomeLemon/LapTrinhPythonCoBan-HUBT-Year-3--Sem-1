class Student:
    def __init__(self):
        self.masv = ""
        self.dtb = 0.0
        self.tuoi = 0
        self.lop = ""

    def Info(self):
        while True:
            self.masv = input("Nhập mã sinh viên (đúng 8 ký tự): ")
            if len(self.masv) == 8:
                break
            print("Mã sinh viên phải chứa đúng 8 ký tự! Vui lòng nhập lại.")

        while True:
            self.dtb = float(input("Nhập điểm trung bình (0.0 - 10.0): "))
            if 0.0 <= self.dtb <= 10.0:
                break
            print("Điểm trung bình không hợp lệ!")

        while True:
            self.tuoi = int(input("Nhập tuổi (>= 18): "))
            if self.tuoi >= 18:
                break
            print("Tuổi phải lớn hơn hoặc bằng 18!")

        while True:
            self.lop = input("Nhập tên lớp (bắt đầu bằng 'A' hoặc 'C'): ")
            if self.lop.startswith('A') or self.lop.startswith('C'):
                break
            print("Tên lớp phải bắt đầu bằng 'A' hoặc 'C'!")

    def ShowInfo(self):
        print(f"Mã SV: {self.masv} | Tên lớp: {self.lop} | Tuổi: {self.tuoi} | ĐTB: {self.dtb}")

    def SortInfo(danh_sach):
        danh_sach.sort(key=lambda x: x.dtb)
        print("\n--- Đã sắp xếp sinh viên theo ĐTB tăng dần ---")


    def SearchInfo(danh_sach):
        ma = input("Nhập mã sinh viên cần tìm: ")
        found = False
        for sv in danh_sach:
            if sv.masv == ma:
                print("Tìm thấy sinh viên:")
                sv.ShowInfo()
                found = True
                break
        if not found:
            print("Không tìm thấy sinh viên có mã này!")

    def MaxInfo(danh_sach):
        ten_lop = input("Nhập tên lớp cần tìm sinh viên điểm cao nhất: ")
        lop_loc = [sv for sv in danh_sach if sv.lop == ten_lop]
        if not lop_loc:
            print("Không có sinh viên nào trong lớp này!")
            return
        max_sv = max(lop_loc, key=lambda x: x.dtb)
        print(f"Sinh viên điểm cao nhất lớp {ten_lop}:")
        max_sv.ShowInfo()

ds = []
std = Student()
n = int(input("Nhập số sinh viên cần nhập: "))
for i in range(n):
    std.Info()
    ds.append(std)

for std in ds:
    std.ShowInfo()

# std.SortInfo()
# std.SearchInfo()
# std.MaxInfo()