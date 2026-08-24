diem = {
    "SV01": 8.5,
    "SV02": 7.0,
    "SV03": 9.0
}

def them():
    ma = input("Nhập mã sinh viên: ")
    d = float(input("Nhập điểm: "))
    diem[ma] = d
    print("Đã thêm sinh viên.")

def capNhat():
    ma = input("Nhập mã sinh viên cần cập nhật: ")
    if ma in diem:
        d = float(input("Nhập điểm mới: "))
        diem[ma] = d
        print("Đã cập nhật điểm.")
    else:
        print("Không tìm thấy sinh viên.")

def xoa():
    ma = input("Nhập mã sinh viên cần xóa: ")
    if ma in diem:
        del diem[ma]
        print("Đã xóa sinh viên.")
    else:
        print("Không tìm thấy sinh viên.")

def timKiem():
    ma = input("Nhập mã sinh viên cần tìm: ")
    if ma in diem:
        print(f"""
Mã sinh viên: {ma}
Điểm: {diem[ma]}
""")
    else:
        print("Không tìm thấy sinh viên.")

def xemDiemCaoNhat():
    diemCaoNhat = max(diem.values())
    print("Sinh viên có điểm cao nhất:")
    for ma in diem:
        if diem[ma] == diemCaoNhat:
            print(f"Mã: {ma} - Điểm: {diem[ma]}")

def tinhTrungBinh():
    tong = 0
    for d in diem.values():
        tong += d
    trungBinh = tong / len(diem)
    print("Điểm trung bình:", trungBinh)

while True:
    print("""
===== QUẢN LÝ ĐIỂM =====
1. Thêm sinh viên
2. Cập nhật điểm
3. Xóa sinh viên
4. Tìm điểm theo mã
5. Tìm điểm cao nhất
6. Tính điểm trung bình
0. Thoát
""")

    chon = int(input("Nhập lựa chọn: "))
    match chon:
        case 1:
            them()
        case 2:
            capNhat()
        case 3:
            xoa()
        case 4:
            timKiem()
        case 5:
            xemDiemCaoNhat()
        case 6:
            tinhTrungBinh()
        case 0:
            break
        case _:
            print("Không hợp lệ")