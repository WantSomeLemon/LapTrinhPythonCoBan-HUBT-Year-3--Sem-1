ds = []

def them():
    ma = input("Nhập mã sản phẩm: ")
    ten = input("Nhập tên sản phẩm: ")
    gia = float(input("Nhập giá sản phẩm: "))
    ds.append([ma, ten, gia])
    print("Đã thêm sản phẩm.")

def xoa():
    if len(ds) == 0:
        print("Danh sách rỗng.")
        return

    ma = input("Nhập mã sản phẩm cần xóa: ")
    for sp in ds:
        if sp[0] == ma:
            ds.remove(sp)
            print("Đã xóa sản phẩm.")
            return
    print("Không tìm thấy sản phẩm.")

def sua():
    if len(ds) == 0:
        print("Danh sách rỗng.")
        return

    ma = input("Nhập mã sản phẩm cần sửa: ")
    for sp in ds:
        if sp[0] == ma:
            sp[1] = input("Nhập tên mới: ")
            sp[2] = float(input("Nhập giá mới: "))
            print("Đã sửa sản phẩm.")
            return
    print("Không tìm thấy sản phẩm.")

def timKiem():
    if len(ds) == 0:
        print("Danh sách rỗng.")
        return

    ten = input("Nhập tên sản phẩm cần tìm: ")
    for sp in ds:
        if sp[1].lower() == ten.lower():
            print(f"""
Mã sản phẩm: {sp[0]}
Tên sản phẩm: {sp[1]}
Giá sản phẩm: {sp[2]}
""")
            return
    print("Không tìm thấy sản phẩm.")

def sapXep():
    if len(ds) == 0:
        print("Danh sách rỗng.")
        return

    ds.sort(key=lambda sp: sp[2])
    print("Đã sắp xếp theo giá tăng dần.")
    for sp in ds:
        print(f"Mã: {sp[0]} - Tên: {sp[1]} - Giá: {sp[2]}")

def sanPhamDatNhat():
    if len(ds) == 0:
        print("Danh sách rỗng.")
        return

    spDatNhat = ds[0]
    for sp in ds:
        if sp[2] > spDatNhat[2]:
            spDatNhat = sp
    print(f"""
Sản phẩm đắt nhất:
Mã: {spDatNhat[0]}
Tên: {spDatNhat[1]}
Giá: {spDatNhat[2]}
""")

while True:
    print("""
===== QUẢN LÝ SẢN PHẨM =====
1. Thêm sản phẩm
2. Xóa sản phẩm
3. Sửa sản phẩm
4. Tìm kiếm sản phẩm
5. Sắp xếp theo giá
6. Tìm sản phẩm đắt nhất
0. Thoát
""")

    chon = int(input("Nhập lựa chọn: "))
    match chon:
        case 1:
            them()
        case 2:
            xoa()
        case 3:
            sua()
        case 4:
            timKiem()
        case 5:
            sapXep()
        case 6:
            sanPhamDatNhat()
        case 0:
            break
        case _:
            print("Không hợp lệ")