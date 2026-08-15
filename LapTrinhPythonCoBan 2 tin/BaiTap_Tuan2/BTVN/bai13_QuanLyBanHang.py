from unittest import case

ma_sp = []
ten_sp = []
don_gia = []
so_luong = []

doanh_thu = 0


def nhap_san_pham():
    n = int(input("Nhập số sản phẩm muốn nhập: "))
    while n < 0:
        print("Lại Âm")
        n = int(input("Nhập số sản phẩm muốn nhập: "))

    for i in range(n):
        print(f"\n--- Sản phẩm {i + 1} ---")
        ma = input("Mã sản phẩm: ")

        # Kiểm tra mã sản phẩm đã tồn tại chưa
        if ma in ma_sp:
            print("Mã sản phẩm đã tồn tại!")
            continue

        ten = input("Tên sản phẩm: ")
        gia = float(input("Đơn giá: "))
        sl = int(input("Số lượng: "))

        ma_sp.append(ma)
        ten_sp.append(ten)
        don_gia.append(gia)
        so_luong.append(sl)

        print("Nhập sản phẩm thành công!")


def ban_hang():
    global doanh_thu

    ma = input("Nhập mã sản phẩm cần bán: ")

    # Kiểm tra sản phẩm tồn tại
    if ma not in ma_sp:
        print("Không tìm thấy sản phẩm!")
        return

    vi_tri = ma_sp.index(ma)

    # Nhập số lượng bán
    sl_ban = int(input("Nhập số lượng cần bán: "))

    # Kiểm tra số lượng tồn kho
    if sl_ban > so_luong[vi_tri]:
        print("Không đủ số lượng trong kho!")
        print("Số lượng tồn kho:", so_luong[vi_tri])
        return

    if sl_ban <= 0:
        print("Số lượng bán phải lớn hơn 0!")
        return

    # Tính thành tiền
    thanh_tien = sl_ban * don_gia[vi_tri]

    # Cập nhật số lượng tồn
    so_luong[vi_tri] -= sl_ban

    # Cập nhật doanh thu
    doanh_thu += thanh_tien

    print("\n===== HÓA ĐƠN =====")
    print("Mã sản phẩm:", ma_sp[vi_tri])
    print("Tên sản phẩm:", ten_sp[vi_tri])
    print("Đơn giá:", don_gia[vi_tri])
    print("Số lượng bán:", sl_ban)
    print("Thành tiền:", thanh_tien)
    print("Tồn kho:", so_luong[vi_tri])


def tinh_doanh_thu():
    print("\n===== DOANH THU =====")
    print("Tổng doanh thu:", doanh_thu)


def kiem_tra_ton_kho():
    print("\n===== TỒN KHO =====")

    if len(ma_sp) == 0:
        print("Chưa có sản phẩm!")
        return

    for i in range(len(ma_sp)):
        print("---------------------------")
        print("Mã sản phẩm:", ma_sp[i])
        print("Tên sản phẩm:", ten_sp[i])
        print("Đơn giá:", don_gia[i])
        print("Số lượng tồn:", so_luong[i])


def thong_ke():
    print("\n===== THỐNG KÊ =====")

    if len(ma_sp) == 0:
        print("Chưa có sản phẩm!")
        return

    tong_so_luong = 0
    tong_gia_tri = 0

    for i in range(len(ma_sp)):
        tong_so_luong += so_luong[i]
        tong_gia_tri += so_luong[i] * don_gia[i]

    print("Số loại sản phẩm:", len(ma_sp))
    print("Tổng số lượng tồn:", tong_so_luong)
    print("Tổng giá trị hàng tồn:", tong_gia_tri)
    print("Doanh thu:", doanh_thu)




while True:
    print("""
    ========= CỬA HÀNG =========
    1. Nhập sản phẩm
    2. Bán hàng
    3. Tính doanh thu
    4. Kiểm tra tồn kho
    5. Thống kê
    6. Thoát
    =============================
    """)

    chon = input("Nhập lựa chọn: ")
    while chon <1 or chon > 6:
        print("Không hợp lệ")
        chon = input("Nhập lựa chọn: ")

    match chon:
        case 1:
            nhap_san_pham()
        case 2:
            ban_hang()
        case 3:
            tinh_doanh_thu()
        case 4:
            kiem_tra_ton_kho()
        case 5:
            thong_ke()
        case 6:
            print("Đã thoát chương trình!")
            break
        case _:
            print("Không biết nữa")