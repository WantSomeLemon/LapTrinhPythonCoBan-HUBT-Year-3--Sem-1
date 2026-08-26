class SACH:
    def __init__(self):
        self.tenSach = ""
        self.tacGia = ""
        self.giaBan = 0.0

    def nhap(self):
        self.tenSach = input("Nhập tên sách: ")
        self.tacGia = input("Nhập tác giả: ")
        self.giaBan = float(input("Nhập giá bán: "))

    def inDuLieu(self):
        print(f"Tên sách: {self.tenSach} |"
              f" Tác giả: {self.tacGia} |"
              f" Giá: {self.giaBan:,.0f}", end=" ")

class BIA:
    def __init__(self):
        self.maHinhAnh = ""
        self.tien_ve = 0.0

    def nhap(self):
        self.maHinhAnh = input("Nhập mã hình ảnh: ")
        self.tien_ve = float(input("Nhập tiền vẽ bìa: "))

    def inDuLieu(self):
        print(f"| Mã hình: {self.maHinhAnh} | Tiền vẽ: {self.tien_ve:,.0f}", end=" ")

class HOASY:
    def __init__(self):
        self.tenHoaSy = ""
        self.diaChiHoaSy = ""

    def nhap(self):
        self.tenHoaSy = input("Nhập tên họa sỹ: ")
        self.diaChiHoaSy = input("Nhập địa chỉ họa sỹ: ")

    def inDuLieu(self):
        print(f"| Họa sỹ: {self.tenHoaSy}")

class SACHVEBIA(SACH, BIA, HOASY):
    def __init__(self):
        SACH.__init__(self)
        BIA.__init__(self)
        HOASY.__init__(self)

    def nhap(self):
        SACH.nhap(self)
        BIA.nhap(self)
        HOASY.nhap(self)

    def tong_tien(self):
        return self.giaBan + self.tien_ve

    def inDuLieu(self):
        SACH.inDuLieu(self)
        BIA.inDuLieu(self)
        HOASY.inDuLieu(self)
        print(f"  -> Tổng tiền: {self.tong_tien():,.0f}\n")

# Console
ds = []
n = int(input("Nhập số lượng sách có vẽ bìa: "))
for i in range(n):
    print(f"\nNhập sách có vẽ bìa thứ {i+1}:")
    s = SACHVEBIA()
    s.nhap()
    ds.append(s)

print("\n--- DANH SÁCH SÁCH CÓ VẼ BÌA ---")
for s in ds:
    s.inDuLieu()

x = input("Nhập tên tác giả cần tìm sách có vẽ hình: ")
found = False
for s in ds:
    if s.tacGia.lower() == x.lower():
        s.inDuLieu()
        found = True
if not found:
    print("Không có cuốn sách nào của tác giả này!")