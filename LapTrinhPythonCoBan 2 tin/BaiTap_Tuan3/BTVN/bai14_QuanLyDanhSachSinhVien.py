ds = []
sinhVien = ("SV01", "Nguyen Van An", 20, 8.5)

def them():
    ma = input("Nhập mã sinh viên: ")
    ten = input("Nhập tên sinh viên: ")
    tuoi = int(input("Nhập tuổi sinh viên: "))
    ds.append([ma, ten, tuoi])
    print("Đã thêm sinh viên.")

def xoa():
    if len(ds) == 0:
        print("Danh sách rỗng.")
        return

    ma = input("Nhập mã sinh viên cần xóa: ")
    for sv in ds:
        if sv[0] == ma:
            ds.remove(sv)
            print("Đã xóa sinh viên.")
            return
    print("Không tìm thấy sinh viên.")

def sua():
    if len(ds) == 0:
        print("Danh sách rỗng.")
        return

    ma = input("Nhập mã sinh viên cần sửa: ")
    for sv in ds:
        if sv[0] == ma:
            sv[1] = input("Nhập tên mới: ")
            sv[2] = int(input("Nhập tuổi mới: "))
            print("Đã sửa sinh viên.")
        return
    print("Không tìm thấy sinh viên.")

def xem():
    if len(ds) == 0:
        print("Danh sách rỗng.")
    else:
        print("\n===== DANH SÁCH SINH VIÊN =====")
        for sv in ds:
            print(f"""
Mã sinh viên: {sv[0]}
Tên sinh viên: {sv[1]}
Tuổi: {sv[2]}
""")

def timKiem():
    if len(ds) == 0:
        print("Danh sách rỗng.")
        return

    ma = input("Nhập mã sinh viên cần tìm: ")

    for sv in ds:
        if sv[0] == ma:
            print(f"""
Mã sinh viên: {sv[0]}
Tên sinh viên: {sv[1]}
Tuổi: {sv[2]}
""")
            return
    print("Không tìm thấy sinh viên.")

while True:
    print("""
===== QUẢN LÝ SINH VIÊN =====
1. Thêm sinh viên
2. Xóa sinh viên
3. Sửa sinh viên
4. Xem danh sách sinh viên
5. Tìm kiếm sinh viên
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
            xem()
        case 5:
            timKiem()
        case 0:
            break
        case _:
            print("Không hợp lệ")