sanPham = {
    "SP01": {
        "ten": "Laptop",
        "gia": 15000000,
        "so_luong": 10
    }
}

def them():
    ma = input("Nhập mã sản phẩm: ")
    ten = input("Nhập tên sản phẩm: ")
    gia = float(input("Nhập giá sản phẩm: "))
    soLuong = int(input("Nhập số lượng: "))
    sanPham[ma] = {
        "ten": ten,
        "gia": gia,
        "so_luong": soLuong
    }
    print("Đã thêm sản phẩm.")

def xoa():
    ma = input("Nhập mã sản phẩm cần xóa: ")
    if ma in sanPham:
        del sanPham[ma]
        print("Đã xóa sản phẩm.")
    else:
        print("Không tìm thấy sản phẩm.")

def capNhatGia():
    ma = input("Nhập mã sản phẩm cần cập nhật giá: ")
    if ma in sanPham:
        gia = float(input("Nhập giá mới: "))
        sanPham[ma]["gia"] = gia
        print("Đã cập nhật giá.")
    else:
        print("Không tìm thấy sản phẩm.")

def capNhatSoLuong():
    ma = input("Nhập mã sản phẩm cần cập nhật số lượng: ")
    if ma in sanPham:
        soLuong = int(input("Nhập số lượng mới: "))
        sanPham[ma]["so_luong"] = soLuong
        print("Đã cập nhật số lượng.")
    else:
        print("Không tìm thấy sản phẩm.")

def timKiem():
    ma = input("Nhập mã sản phẩm cần tìm: ")
    if ma in sanPham:
        sp = sanPham[ma]
        print(f"""
Mã sản phẩm: {ma}
Tên sản phẩm: {sp["ten"]}
Giá: {sp["gia"]}
Số lượng: {sp["so_luong"]}
""")
    else:
        print("Không tìm thấy sản phẩm.")

def tinhGiaTriKho():
    tong = 0
    for ma in sanPham:
        tong += sanPham[ma]["gia"] * sanPham[ma]["so_luong"]
    print("Tổng giá trị kho:", tong)

while True:
    print("""
===== QUẢN LÝ SẢN PHẨM =====
1. Thêm sản phẩm
2. Xóa sản phẩm
3. Cập nhật giá
4. Cập nhật số lượng
5. Tìm sản phẩm
6. Tính giá trị kho
0. Thoát
""")

    chon = int(input("Nhập lựa chọn: "))
    match chon:
        case 1:
            them()
        case 2:
            xoa()
        case 3:
            capNhatGia()
        case 4:
            capNhatSoLuong()
        case 5:
            timKiem()
        case 6:
            tinhGiaTriKho()
        case 0:
            break
        case _:
            print("Không hợp lệ")