ds = [
    ("SP01", "Chuột Logitech", 350000),
    ("SP02", "Bàn phím", 500000),
    ("SP03", "Tai nghe", 750000),
    ("SP04", "Webcam", 650000)
]

def timKiem():
    ma = input("Nhập mã sản phẩm cần tìm: ")
    for sp in ds:
        if sp[0] == ma:
            print(f"""
Mã sản phẩm: {sp[0]}
Tên sản phẩm: {sp[1]}
Giá sản phẩm: {sp[2]}
""")
            return
    print("Không tìm thấy sản phẩm.")

def timDatNhat():
    spDatNhat = ds[0]
    for sp in ds:
        if sp[2] > spDatNhat[2]:
            spDatNhat = sp
    print(f"""
Sản phẩm có giá cao nhất:
Mã sản phẩm: {spDatNhat[0]}
Tên sản phẩm: {spDatNhat[1]}
Giá sản phẩm: {spDatNhat[2]}
""")

def sapXep():
    dsSapXep = sorted(ds, key=lambda sp: sp[2])
    print("Danh sách sản phẩm sau khi sắp xếp:")
    for sp in dsSapXep:
        print(f"""
Mã: {sp[0]}
Tên: {sp[1]}
Giá: {sp[2]}
""")

while True:
    print("""
===== QUẢN LÝ SẢN PHẨM =====
1. Tìm sản phẩm theo mã
2. Tìm sản phẩm có giá cao nhất
3. Sắp xếp sản phẩm theo giá
0. Thoát
""")

    chon = int(input("Nhập lựa chọn: "))
    match chon:
        case 1:
            timKiem()
        case 2:
            timDatNhat()
        case 3:
            sapXep()
        case 0:
            break
        case _:
            print("Không hợp lệ")
