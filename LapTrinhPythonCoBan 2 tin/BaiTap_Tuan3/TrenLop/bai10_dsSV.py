ds = []

def them():
    ma = input("Nhập mã sinh viên: ")
    ten = input("Nhập tên sinh viên: ")

    ds.append([ma, ten])

def xoa():
    ma = input("Nhập mã cần xóa: ")

    for sv in ds:
        if sv[0] == ma:
            ds.remove(sv)
            print("Đã xóa.")
            return

    print("Không tìm thấy sinh viên.")

def sua():
    ma = input("Nhập mã cần sửa: ")

    for sv in ds:
        if sv[0] == ma:
            sv[1] = input("Nhập tên mới: ")
            print("Đã sửa.")
            return

    print("Không tìm thấy sinh viên.")

def xem():
    if len(ds) == 0:
        print("Danh sách rỗng.")
    else:
        print("\nDanh sách sinh viên")
        for sv in ds:
            print("Mã:", sv[0], "- Tên:", sv[1])


while True:
    print("""
===== QUẢN LÝ SINH VIÊN =====
1. Thêm sinh viên
2. Xóa sinh viên
3. Sửa sinh viên
4. Xem danh sách sinh viên
0. Thoát
""")
    chon = int(input("Nhập lựa chọn: "))

    match chon:
        case 1: them()
        case 2: xoa()
        case 3: sua()
        case 4: xem()
        case _: print("Không hợp lệ")