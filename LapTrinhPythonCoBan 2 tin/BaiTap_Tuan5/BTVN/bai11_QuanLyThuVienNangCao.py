class TAILIEU:
    def __init__(self):
        self.ma = ""
        self.ten = ""
        self.nhaXuatBan = ""
        self.namXuatBan = 0

    def nhap(self):
        self.ma = input("Nhập mã tài liệu: ")
        self.ten = input("Nhập tên tài liệu: ")
        self.nhaXuatBan = input("Nhập nhà xuất bản: ")
        self.namXuatBan = int(input("Nhập năm xuất bản: "))

    def xuat(self):
        print(f"Mã: {self.ma} | "
              f"Tên: {self.ten} | "
              f"Nhà xuất bản: {self.nhaXuatBan} | "
              f"Năm xuất bản: {self.namXuatBan}", end=" | ")

class SACH(TAILIEU):
    def __init__(self):
        super().__init__()
        self.tacGia = ""
        self.soTrang = 0

    def nhap(self):
        super().nhap()
        self.tacGia = input("Nhập tác giả: ")
        self.soTrang = int(input("Nhập số trang: "))

    def xuat(self):
        super().xuat()
        print(f"Tác giả: {self.tacGia} | "
              f"Số trang: {self.soTrang}")

class TAPCHI(TAILIEU):
    def __init__(self):
        super().__init__()
        self.soPhatHanh = 0
        self.thangPhatHanh = 0

    def nhap(self):
        super().nhap()
        self.soPhatHanh = int(input("Nhập số phát hành: "))
        self.thangPhatHanh = int(input("Nhập tháng phát hành: "))

    def xuat(self):
        super().xuat()
        print(f"Số phát hành: {self.soPhatHanh} | "
              f"Tháng phát hành: {self.thangPhatHanh}")

class BAO(TAILIEU):
    def __init__(self):
        super().__init__()
        self.ngayPhatHanh = ""

    def nhap(self):
        super().nhap()
        self.ngayPhatHanh = input("Nhập ngày phát hành: ")

    def xuat(self):
        super().xuat()
        print(f"Ngày phát hành: {self.ngayPhatHanh}")

# Console
dsTaiLieu = []
n = int(input("Nhập số lượng tài liệu: "))
for i in range(n):
    print(f"\nTài liệu thứ {i + 1}")
    print("1. Sách")
    print("2. Tạp chí")
    print("3. Báo")
    loai = int(input("Chọn loại tài liệu: "))
    if loai == 1:
        tl = SACH()
    elif loai == 2:
        tl = TAPCHI()
    else:
        tl = BAO()
    tl.nhap()
    dsTaiLieu.append(tl)
print("\n--- DANH SÁCH TÀI LIỆU ---")
for tl in dsTaiLieu:
    tl.xuat()

# Tìm tài liệu theo tên
tenCanTim = input("\nNhập tên tài liệu cần tìm: ")
print("\n--- TÀI LIỆU TÌM ĐƯỢC ---")
found = False
for tl in dsTaiLieu:
    if tl.ten.lower() == tenCanTim.lower():
        tl.xuat()
        found = True
if not found:
    print("Không tìm thấy tài liệu!")

# Tìm sách theo tác giả
tacGiaCanTim = input("\nNhập tên tác giả cần tìm: ")
print("\n--- SÁCH CỦA TÁC GIẢ ---")
found = False
for tl in dsTaiLieu:
    if isinstance(tl, SACH):
        if tl.tacGia.lower() == tacGiaCanTim.lower():
            tl.xuat()
            found = True
if not found:
    print("Không tìm thấy sách của tác giả này!")

# Tài liệu có năm xuất bản mới nhất
if dsTaiLieu:
    namMoiNhat = max(tl.namXuatBan for tl in dsTaiLieu)
    print(f"\n--- TÀI LIỆU MỚI NHẤT ({namMoiNhat}) ---")
    for tl in dsTaiLieu:
        if tl.namXuatBan == namMoiNhat:
            tl.xuat()

# Đếm từng loại
soSach = 0
soTapChi = 0
soBao = 0
for tl in dsTaiLieu:
    if isinstance(tl, SACH):
        soSach += 1
    elif isinstance(tl, TAPCHI):
        soTapChi += 1
    elif isinstance(tl, BAO):
        soBao += 1
print("\n--- SỐ LƯỢNG TỪNG LOẠI ---")
print(f"Số sách: {soSach}")
print(f"Số tạp chí: {soTapChi}")
print(f"Số báo: {soBao}")

# Sắp xếp năm xuất bản giảm dần
dsTaiLieu.sort(key=lambda x: x.namXuatBan, reverse=True)

print("\n--- DANH SÁCH SAU KHI SẮP XẾP ---")
for tl in dsTaiLieu:
    tl.xuat()