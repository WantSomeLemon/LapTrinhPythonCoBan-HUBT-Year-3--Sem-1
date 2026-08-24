def tinhTien(gia, soLuong=1, giamGia=0):
    tongTien = gia * soLuong
    tienGiam = tongTien * giamGia
    thanhTien = tongTien - tienGiam
    return thanhTien

print(f"""
100000:{tinhTien(100000)}
100000, 3:{tinhTien(100000, 3)}
100000, 3, 0.1:{tinhTien(100000, 3, 0.1)}
""")