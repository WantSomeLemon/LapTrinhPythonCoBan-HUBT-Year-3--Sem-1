n = int(input("Nhập số nhân viên: "))
while n <= 0:
    print("Không hợp lệ, nhập lại")
    n = int(input("Nhập số nhân viên: "))

gioLam = []
ketQua = []

for i in range(n):
    gio = float(input(f"Nhập số giờ làm của nhân viên {i + 1}: "))
    while gio <= 0:
        print("Không hợp lệ, nhập lại")
        gio = float(input(f"Nhập số giờ làm của nhân viên {i + 1}: "))
    gioLam.append(gio)

soDuGio = 0
soTangCa = 0

for i in range(n):
    gio = gioLam[i]

    if gio >= 40:
        loai = "Đủ giờ"
        soDuGio += 1
    elif gio >= 30:
        loai = "Thiếu giờ"
    else:
        loai = "Thiếu nhiều"

    if gio > 48:
        tang_ca = "Có tăng ca"
        soTangCa += 1
    else:
        tang_ca = "Không tăng ca"
    ketQua.append(f"Nhân viên {i + 1}: {gio} giờ - {loai} - {tang_ca}")

# nhan vien co gio lam cao nhat
gio_max = max(gioLam)
nhanVienMax = []

for i in range(n):
    if gioLam[i] == gio_max:
        nhanVienMax.append(f"Nhân viên {i + 1}: {gio_max} giờ")

print("--- KẾT QUẢ ---")

for kq in ketQua:
    print(kq)

print(f"""
--- THỐNG KÊ ---

Số nhân viên đủ giờ: {soDuGio}
Số nhân viên tăng ca: {soTangCa}
Số giờ làm cao nhất: {gio_max} giờ
""")

print("Nhân viên có số giờ làm cao nhất:", *nhanVienMax)