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
              f" Giá bán: {self.giaBan:,.0f} VNĐ", end=" | ")

class BIA(SACH):
    def __init__(self):
        super().__init__()
        self.maHinhAnh = ""
        self.tienVe = 0.0

    def nhap(self):
        super().nhap()
        self.maHinhAnh = input("Nhập mã hình ảnh: ")
        self.tienVe = float(input("Nhập tiền vẽ bìa: "))

    def inDuLieu(self):
        super().inDuLieu()
        print(f"Mã hình ảnh: {self.maHinhAnh} |"
              f" Tiền vẽ: {self.tienVe:,.0f} VNĐ", end=" | ")

class HOASY:
    def __init__(self):
        self.tenHoaSy = ""
        self.diaChiHoaSy = ""

    def nhap(self):
        self.tenHoaSy = input("Nhập tên họa sỹ: ")
        self.diaChiHoaSy = input("Nhập địa chỉ họa sỹ: ")

    def inDuLieu(self):
        print(f"Họa sỹ: {self.tenHoaSy} |"
              f" Địa chỉ: {self.diaChiHoaSy}", end=" | ")

class SACHVEBIA(BIA, HOASY):
    def __init__(self):
        BIA.__init__(self)
        HOASY.__init__(self)

    def nhap(self):
        BIA.nhap(self)
        HOASY.nhap(self)

    def tongTien(self):
        return self.giaBan + self.tienVe

    def inDuLieu(self):
        BIA.inDuLieu(self)
        HOASY.inDuLieu(self)
        print(f"Tổng tiền: {self.tongTien():,.0f} VNĐ")

# Console
dsCoBia = []
dsKhongBia = []

n = int(input("Nhập số sách có vẽ bìa: "))
for i in range(n):
    print(f"\nNhập sách có vẽ bìa thứ {i + 1}:")
    s = SACHVEBIA()
    s.nhap()
    dsCoBia.append(s)

n = int(input("\nNhập số sách không có vẽ bìa: "))
for i in range(n):
    print(f"\nNhập sách không có bìa thứ {i + 1}:")
    s = SACH()
    s.nhap()
    dsKhongBia.append(s)

print("\n--- DANH SÁCH SÁCH CÓ VẼ BÌA ---")
for s in dsCoBia:
    s.inDuLieu()
dsKhongBia.sort(key=lambda x: x.giaBan)

print("\n--- DANH SÁCH SÁCH KHÔNG CÓ BÌA ---")
for s in dsKhongBia:
    s.inDuLieu()
    print()

x = input("\nNhập tên tác giả cần tìm: ")
found = False
for s in dsCoBia:
    if s.tacGia.lower() == x.lower():
        s.inDuLieu()
        found = True
if not found:
    print("Không có cuốn sách nào của tác giả này!")