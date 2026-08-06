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


