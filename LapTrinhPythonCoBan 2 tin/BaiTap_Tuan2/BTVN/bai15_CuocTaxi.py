print("""
--- CHỌN LOẠI XE ---

1. Xe 4 chỗ
2. Xe 7 chỗ
3. Xe cao cấp
""")

loaiXe = int(input("Chọn loại xe: "))

while loaiXe < 1 or loaiXe > 3:
    print("Không hợp lệ, nhập lại")
    loaiXe = int(input("Chọn loại xe: "))
'''
bảng giá tự làm
Loại xe	    0–1 km	    Trên 1–10 km    Trên 10 km
Xe 4 chỗ    15.000	    13.000/km       11.000/km
Xe 7 chỗ    17.000	    15.000/km       13.000/km
Xe cao cấp  25.000	    20.000/km       18.000/km
'''

match loaiXe:
    case 1:
        gia1 = 15000
        gia2 = 13000
        gia3 = 11000
        tenXe = "Xe 4 chỗ"

    case 2:
        gia1 = 17000
        gia2 = 15000
        gia3 = 13000
        tenXe = "Xe 7 chỗ"

    case 3:
        gia1 = 25000
        gia2 = 20000
        gia3 = 18000
        tenXe = "Xe cao cấp"

km = float(input("Nhập số km đã đi: "))
while km <= 0:
    print("Không hợp lệ, nhập lại")
    km = float(input("Nhập số km đã đi: "))

if km <= 1:
    tien = gia1

elif km <= 10:
    tien = gia1 + (km - 1) * gia2

else:
    tien = gia1 + 9 * gia2 + (km - 10) * gia3

if km > 30:
    tien = tien * 0.95
print(f"""
--- KẾT QUẢ ---
Loại xe: {tenXe}
Số km đã đi: {km} km
Tổng tiền: {tien:,.0f} VNĐ
""")