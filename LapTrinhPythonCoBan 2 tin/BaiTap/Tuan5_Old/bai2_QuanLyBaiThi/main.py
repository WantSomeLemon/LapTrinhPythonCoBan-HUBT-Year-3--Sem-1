from pip._internal import models

import models

ds_sinh_vien = []

n = int(input("Nhập số lượng sinh viên: "))

if n > 100:
    n = 100
    print("Số lượng sinh viên tối đa là 100.")

for i in range(n):
    print(f"\n--- Nhập sinh viên thứ {i + 1} ---")

    sv = models.KetQua()
    sv.nhap()

    ds_sinh_vien.append(sv)


# Xuat ds
print("\n========== KẾT QUẢ THI ==========")

for i, sv in enumerate(ds_sinh_vien, 1):
    print(f"\n--- Sinh viên {i} ---")
    sv.xuat()