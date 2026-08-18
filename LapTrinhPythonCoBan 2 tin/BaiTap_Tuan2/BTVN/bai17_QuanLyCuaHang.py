# sanPham[] = (Tên sản phẩm, Giá bán, Số lượng [tồn kho], Doanh thu)
sanPham = []
doanhThu = 0

def hienThiSanPham(sp, i):
    print(f"""{i + 1}. {sp["ten"]} - {sp["gia"]:.0f} đồng - Tồn: {sp["soLuong"]}""")


def timSanPham(sanPham, ten):
    for i in range(len(sanPham)):
        if sanPham[i]["ten"].lower() == ten.lower():
            return i
    return -1


while True:
    print("""
========================================
       QUẢN LÝ CỬA HÀNG TIỆN LỢI
========================================
1. Nhập thông tin sản phẩm
2. Hiển thị sản phẩm
3. Tìm sản phẩm
4. Bán sản phẩm
5. Nhập thêm hàng
6. Thống kê doanh thu
7. Thống kê tồn kho
8. Thoát
========================================
""")

    luaChon = int(input("Nhập lựa chọn: "))
    while luaChon < 1 or luaChon > 8:
        print("Không hợp lệ, nhập lại")
        luaChon = int(input("Nhập lựa chọn: "))

    match luaChon:
        # 1. Nhập thông tin sản phẩm
        case 1:
            ten = input("Nhập tên sản phẩm: ")
            gia = float(input("Nhập giá bán: "))
            while gia <= 0:
                print("Giá không hợp lệ, nhập lại")
                gia = float(input("Nhập giá bán: "))

            soLuong = int(input("Nhập số lượng: "))
            while soLuong < 0:
                print("Số lượng không hợp lệ, nhập lại")
                soLuong = int(input("Nhập số lượng: "))

            sanPham.append({
                "ten": ten,
                "gia": gia,
                "soLuong": soLuong
            })
            print("Đã thêm sản phẩm thành công!")

        # 2. Hiển thị sản phẩm
        case 2:
            if len(sanPham) == 0:
                print("Chưa có sản phẩm.")
            else:
                print("--- DANH SÁCH SẢN PHẨM ---")
                for i in range(len(sanPham)):
                    hienThiSanPham(sanPham[i], i)

        # 3. Tìm sản phẩm
        case 3:
            if len(sanPham) == 0:
                print("Chưa có sản phẩm.")
            else:
                tenTim = input("Nhập tên sản phẩm cần tìm: ")
                viTri = timSanPham(sanPham, tenTim)

                if viTri == -1:
                    print("Không tìm thấy sản phẩm.")
                else:
                    print("--- SẢN PHẨM TÌM THẤY ---")
                    hienThiSanPham(sanPham[viTri], viTri)

        # 4. Bán sản phẩm
        case 4:
            if len(sanPham) == 0:
                print("Chưa có sản phẩm.")
                continue

            tenBan = input("Nhập tên sản phẩm cần bán: ")
            viTri = timSanPham(sanPham, tenBan)

            if viTri == -1:
                print("Không tìm thấy sản phẩm.")
                continue

            if sanPham[viTri]["soLuong"] == 0:
                print("Sản phẩm đã hết hàng.")
                continue

            soLuongBan = int(input("Nhập số lượng bán: "))

            while soLuongBan <= 0:
                print("Số lượng không hợp lệ, nhập lại")
                soLuongBan = int(input("Nhập số lượng bán: "))

            if soLuongBan > sanPham[viTri]["soLuong"]:
                print("Không đủ hàng trong kho.")
            else:
                sanPham[viTri]["soLuong"] -= soLuongBan
                tien = soLuongBan * sanPham[viTri]["gia"]
                doanhThu += tien

                print(f"""--- BÁN HÀNG ---
                Sản phẩm: {sanPham[viTri]["ten"]}
                Số lượng bán: {soLuongBan}
                Tiền thu: {tien:.0f} đồng
                """)

        # 5. Nhập thêm hàng
        case 5:
            if len(sanPham) == 0:
                print("Chưa có sản phẩm.")
                continue

            tenNhap = input("Nhập tên sản phẩm cần nhập thêm: ")
            viTri = timSanPham(sanPham, tenNhap)

            if viTri == -1:
                print("Không tìm thấy sản phẩm.")
                continue

            soLuongNhap = int(input("Nhập số lượng nhập thêm: "))
            while soLuongNhap <= 0:
                print("Số lượng không hợp lệ, nhập lại")
                soLuongNhap = int(input("Nhập số lượng nhập thêm: "))

            sanPham[viTri]["soLuong"] += soLuongNhap

            print(f"""--- NHẬP THÊM HÀNG ---
            Sản phẩm: {sanPham[viTri]["ten"]}
            Số lượng nhập thêm: {soLuongNhap}
            Số lượng tồn: {sanPham[viTri]["soLuong"]}
            """)

        # 6. Thống kê doanh thu
        case 6:
            print(f"""--- THỐNG KÊ DOANH THU ---
            Doanh thu: {doanhThu:.0f} đồng
            """)

            if doanhThu < 5000000:
                print("Mức doanh thu: Thấp")

            elif doanhThu <= 20000000:
                print("Mức doanh thu: Trung bình")

            elif doanhThu <= 50000000:
                print("Mức doanh thu: Khá")

            else:
                print("Mức doanh thu: Cao")

        # 7. Thống kê tồn kho
        case 7:
            if len(sanPham) == 0:
                print("Chưa có sản phẩm.")
                continue

            print("--- THỐNG KÊ TỒN KHO ---")
            for i in range(len(sanPham)):
                soLuong = sanPham[i]["soLuong"]

                if soLuong == 0:
                    trangThai = "Hết hàng"

                elif soLuong <= 10:
                    trangThai = "Sắp hết"

                else:
                    trangThai = "Còn hàng"

                print(f"""
                Sản phẩm: {sanPham[i]["ten"]}
                Số lượng: {soLuong}
                Trạng thái: {trangThai}
                """)

        # 8. Thoát
        case 8:
            print("Xin chào và không gặp lại.")
            break