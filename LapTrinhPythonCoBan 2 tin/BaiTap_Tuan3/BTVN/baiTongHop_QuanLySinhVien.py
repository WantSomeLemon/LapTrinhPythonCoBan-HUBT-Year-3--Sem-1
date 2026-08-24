from datetime import datetime, date
import re

danhSach = []
'''
    sinhVien = {
        "ma": ma,
        "hoTen": hoTen,
        "ngaySinh": ngaySinh,
        "email": email,
        "diemPython": diemPython,
        "diemCsdl": diemCsdl,
        "diemJava": diemJava
    }
'''

def chuanHoaHoTen(hoTen):
    hoTen = hoTen.strip()
    tachTu = hoTen.split()
    hoTen = " ".join(tachTu)
    hoTen = hoTen.title()
    return hoTen

def kiemTraEmail(email):
    mau = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    if re.match(mau, email):
        return True
    else:
        return False

def nhapEmail():
    while True:
        email = input("Nhập email: ")
        if kiemTraEmail(email):
            return email
        print("Email không hợp lệ. Vui lòng nhập lại.")

def nhapNgaySinh():
    while True:
        ngaySinh = input("Nhập ngày sinh (dd/mm/yyyy): ")
        if re.match(r"^\d{2}/\d{2}/\d{4}$", ngaySinh):
            return ngaySinh
        print("Sai định dạng. Vui lòng nhập theo dạng dd/mm/yyyy.")

def tinhTuoi(ngaySinh):
    ngaySinh = datetime.strptime(ngaySinh, "%d/%m/%Y")
    ngayHienTai = date.today()
    tuoi = ngayHienTai.year - ngaySinh.year
    if (ngayHienTai.month, ngayHienTai.day) < (ngaySinh.month,ngaySinh.day):
        tuoi -= 1
    return tuoi

def nhapHoTen():
    while True:
        hoTen = input("Nhập họ tên: ")
        if hoTen.strip() != "":
            return chuanHoaHoTen(hoTen)
        print("Họ tên không được để trống.")

def nhapDiem(mon):
    while True:
        diem = float(input(f"Nhập điểm {mon}: "))
        if 0 <= diem <= 10:
            return diem
        print("Điểm phải từ 0 đến 10.")

def tinhDtb(sinhVien):
    diem = (
        sinhVien["diemPython"],
        sinhVien["diemCsdl"],
        sinhVien["diemJava"]
    )
    dtb = sum(diem) / len(diem)
    return round(dtb, 2)

def xepLoai(dtb):
    if dtb >= 8.5:
        return "Xuất sắc"
    elif dtb >= 7:
        return "Khá"
    elif dtb >= 5:
        return "Trung bình"
    else:
        return "Yếu"

# case 1
def themSinhVien():
    while True:
        ma = input("Nhập mã sinh viên: ")
        if ma == "":
            print("Mã sinh viên không được để trống.")
            continue
        trungMa = False
        for sinhVien in danhSach:
            if sinhVien["ma"] == ma:
                trungMa = True
                break
        if trungMa:
            print("Mã sinh viên đã tồn tại.")
        else:
            break

    hoTen = nhapHoTen()
    ngaySinh = nhapNgaySinh()
    email = nhapEmail()
    diemPython = nhapDiem("Python")
    diemCsdl = nhapDiem("CSDL")
    diemJava = nhapDiem("Java")
    sinhVien = {
        "ma": ma,
        "hoTen": hoTen,
        "ngaySinh": ngaySinh,
        "email": email,
        "diemPython": diemPython,
        "diemCsdl": diemCsdl,
        "diemJava": diemJava
    }
    danhSach.append(sinhVien)
    print("Đã thêm sinh viên.")

# case 2
def hienThiDanhSach():
    if len(danhSach) == 0:
        print("Danh sách rỗng.")
    else:
        print(f"""
================ DANH SÁCH SINH VIÊN ================
""")
        for sinhVien in danhSach:
            dtb = tinhDtb(sinhVien)
            print(f"""
Mã sinh viên: {sinhVien["ma"]}
Họ tên: {sinhVien["hoTen"]}
Ngày sinh: {sinhVien["ngaySinh"]}
Email: {sinhVien["email"]}
Điểm Python: {sinhVien["diemPython"]}
Điểm CSDL: {sinhVien["diemCsdl"]}
Điểm Java: {sinhVien["diemJava"]}
Điểm trung bình: {dtb}
Xếp loại: {xepLoai(dtb)}
""")

# case 3
def timTheoMa():
    ma = input("Nhập mã sinh viên cần tìm: ")
    for sinhVien in danhSach:
        if sinhVien["ma"] == ma:
            dtb = tinhDtb(sinhVien)
            print(f"""
Mã sinh viên: {sinhVien["ma"]}
Họ tên: {sinhVien["hoTen"]}
Ngày sinh: {sinhVien["ngaySinh"]}
Email: {sinhVien["email"]}
Điểm Python: {sinhVien["diemPython"]}
Điểm CSDL: {sinhVien["diemCsdl"]}
Điểm Java: {sinhVien["diemJava"]}
Điểm trung bình: {dtb}
Xếp loại: {xepLoai(dtb)}
""")
            return
    print("Không tìm thấy sinh viên.")

# case 4
def timTheoTen():
    ten = input("Nhập tên cần tìm: ")
    ten = ten.strip().lower()
    if ten == "":
        print("Tên không được để trống.")
        return
    timThay = False
    for sinhVien in danhSach:
        if ten in sinhVien["hoTen"].lower():
            print(f"""
Mã sinh viên: {sinhVien["ma"]}
Họ tên: {sinhVien["hoTen"]}
Ngày sinh: {sinhVien["ngaySinh"]}
Email: {sinhVien["email"]}
""")
            timThay = True
    if not timThay:
        print("Không tìm thấy sinh viên.")

# case 5
def suaSinhVien():
    ma = input("Nhập mã sinh viên cần sửa: ")
    for sinhVien in danhSach:
        if sinhVien["ma"] == ma:
            print("Nhập thông tin mới:")
            sinhVien["hoTen"] = nhapHoTen()
            sinhVien["ngaySinh"] = nhapNgaySinh()
            sinhVien["email"] = nhapEmail()
            sinhVien["diemPython"] = nhapDiem("Python")
            sinhVien["diemCsdl"] = nhapDiem("CSDL")
            sinhVien["diemJava"] = nhapDiem("Java")
            print("Đã sửa thông tin sinh viên.")
            return
    print("Không tìm thấy sinh viên.")

# case 6
def xoaSinhVien():
    ma = input("Nhập mã sinh viên cần xóa: ")
    for sinhVien in danhSach:
        if sinhVien["ma"] == ma:
            while True:
                luaChon = input("Bạn có chắc chắn muốn xóa? (Y/N): ")
                if luaChon.upper() == "Y":
                    danhSach.remove(sinhVien)
                    print("Đã xóa sinh viên.")
                    return
                elif luaChon.upper() == "N":
                    print("Đã hủy.")
                    return
                else:
                    print("Chỉ được nhập Y hoặc N.")
    print("Không tìm thấy sinh viên.")

# case 7
def tinhDiemTrungBinh():
    if len(danhSach) == 0:
        print("Danh sách rỗng.")
    else:
        for sinhVien in danhSach:
            dtb = tinhDtb(sinhVien)
            print(f"""
Mã: {sinhVien["ma"]}
Họ tên: {sinhVien["hoTen"]}
Điểm trung bình: {dtb}
""")

# case 8
def xepLoaiSinhVien():
    if len(danhSach) == 0:
        print("Danh sách rỗng.")
    else:
        for sinhVien in danhSach:
            dtb = tinhDtb(sinhVien)
            loai = xepLoai(dtb)
            print(f"""
Mã: {sinhVien["ma"]}
Họ tên: {sinhVien["hoTen"]}
Điểm trung bình: {dtb}
Xếp loại: {loai}
""")

# case 9
def timDiemCaoNhat():
    if len(danhSach) == 0:
        print("Danh sách rỗng.")
        return
    diemCaoNhat = tinhDtb(danhSach[0])
    for sinhVien in danhSach:
        dtb = tinhDtb(sinhVien)
        if dtb > diemCaoNhat:
            diemCaoNhat = dtb
    print(f"""
================ ĐIỂM CAO NHẤT ================
Điểm cao nhất: {diemCaoNhat}
""")
    for sinhVien in danhSach:
        dtb = tinhDtb(sinhVien)
        if dtb == diemCaoNhat:
            print(f"""
Mã: {sinhVien["ma"]}
Họ tên: {sinhVien["hoTen"]}
Điểm trung bình: {dtb}
""")

# case 10
def sapXepTheoDiem():
    if len(danhSach) == 0:
        print("Danh sách rỗng.")
        return
    while True:
        luaChon = int(input("""
1. Sắp xếp tăng dần
2. Sắp xếp giảm dần
Nhập lựa chọn: """))
        if luaChon == 1:
            danhSach.sort(key=tinhDtb)
            break
        elif luaChon == 2:
            danhSach.sort(key=tinhDtb, reverse=True)
            break
        else:
            print("Không hợp lệ.")
    hienThiDanhSach()

# case 11
def locTheoTuoi():
    while True:
        tuoi = int(input("Nhập tuổi cần tìm: "))
        if tuoi >= 0:
            break
        print("Tuổi không hợp lệ.")
    timThay = False
    for sinhVien in danhSach:
        tuoiSinhVien = tinhTuoi(sinhVien["ngaySinh"])
        if tuoiSinhVien == tuoi:
            print(f"""
Mã: {sinhVien["ma"]}
Họ tên: {sinhVien["hoTen"]}
Ngày sinh: {sinhVien["ngaySinh"]}
Tuổi: {tuoiSinhVien}
""")
            timThay = True
    if not timThay:
        print("Không có sinh viên ở độ tuổi này.")

# case 12
def thongKe():
    if len(danhSach) == 0:
        print("Danh sách rỗng.")
        return
    xuatSac = 0
    kha = 0
    trungBinh = 0
    yeu = 0
    tongDiem = 0
    for sinhVien in danhSach:
        dtb = tinhDtb(sinhVien)
        tongDiem += dtb
        if dtb >= 8.5:
            xuatSac += 1
        elif dtb >= 7:
            kha += 1
        elif dtb >= 5:
            trungBinh += 1
        else:
            yeu += 1
    diemTrungBinhLop = tongDiem / len(danhSach)
    print(f"""
================ THỐNG KÊ ================
Tổng số sinh viên: {len(danhSach)}
Xuất sắc: {xuatSac}
Khá: {kha}
Trung bình: {trungBinh}
Yếu: {yeu}
Điểm trung bình lớp: {diemTrungBinhLop:.2f}
""")

# case 13
def thongKeTenKhongTrung():
    if len(danhSach) == 0:
        print("Danh sách rỗng.")
        return
    danhSachTen = set()
    for sinhVien in danhSach:
        danhSachTen.add(sinhVien["hoTen"])
    print(f"""
Số sinh viên: {len(danhSach)}
Số họ tên khác nhau: {len(danhSachTen)}
""")
    for ten in danhSachTen:
        print(ten)

# --Phan chay chuong trinh--
while True:
    print("""
========================================
       QUẢN LÝ SINH VIÊN
========================================
1. Thêm sinh viên
2. Hiển thị danh sách
3. Tìm sinh viên theo mã
4. Tìm sinh viên theo tên
5. Sửa thông tin sinh viên
6. Xóa sinh viên
7. Tính điểm trung bình
8. Xếp loại sinh viên
9. Tìm sinh viên điểm cao nhất
10. Sắp xếp sinh viên theo điểm
11. Lọc sinh viên theo tuổi
12. Thống kê sinh viên
13. Thống kê tên không trùng
0. Thoát
========================================
""")
    chon = int(input("Nhập lựa chọn: "))
    match chon:
        case 1:
            themSinhVien()
        case 2:
            hienThiDanhSach()
        case 3:
            timTheoMa()
        case 4:
            timTheoTen()
        case 5:
            suaSinhVien()
        case 6:
            xoaSinhVien()
        case 7:
            tinhDiemTrungBinh()
        case 8:
            xepLoaiSinhVien()
        case 9:
            timDiemCaoNhat()
        case 10:
            sapXepTheoDiem()
        case 11:
            locTheoTuoi()
        case 12:
            thongKe()
        case 13:
            thongKeTenKhongTrung()
        case 0:
            print("Đã thoát chương trình.")
            break
        case _:
            print("Không hợp lệ.")