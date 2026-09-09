import models

#Nhap ds sach ve bia
ds_sach_ve_bia = []

n = int(input("Nhập số sách có vẽ bìa: "))

for i in range(n):
    print(f"\n--- Sách vẽ bìa thứ {i + 1} ---")

    sach = models.SACHVEBIA()
    sach.nhap()

    ds_sach_ve_bia.append(sach)

#Nhap ds sach ko ve bia
ds_sach_khong_ve_bia = []

n = int(input("\nNhập số sách không vẽ bìa: "))

for i in range(n):
    print(f"\n--- Sách không vẽ bìa thứ {i + 1} ---")

    sach = models.SACH()
    sach.nhap()

    ds_sach_khong_ve_bia.append(sach)


#In ds sach co bia
print("\n========================================")
print("DANH SÁCH SÁCH CÓ VẼ BÌA")
print("========================================")

for i, sach in enumerate(ds_sach_ve_bia, 1):
    print(f"\n--- Sách {i} ---")
    sach.xuat()

#In ds sach ko co bia
print("\n========================================")
print("DANH SÁCH SÁCH KHÔNG VẼ BÌA")
print("========================================")

for i, sach in enumerate(ds_sach_khong_ve_bia, 1):
    print(f"\n--- Sách {i} ---")
    sach.xuat()

#Sap xep ds sach ko co bia
ds_sach_khong_ve_bia.sort(key=lambda sach: sach.gia_ban)

print("\n========================================")
print("SÁCH KHÔNG VẼ BÌA SAU KHI SẮP XẾP")
print("========================================")

for i, sach in enumerate(ds_sach_khong_ve_bia, 1):
    print(f"\n--- Sách {i} ---")
    sach.xuat()


#Tim tac gia
tac_gia_can_tim = input(
    "\nNhập tên tác giả cần tìm: "
)

tim_thay = False

print("\n========================================")
print("KẾT QUẢ TÌM KIẾM")
print("========================================")

for sach in ds_sach_ve_bia:

    if sach.tac_gia.lower() == tac_gia_can_tim.lower():

        sach.xuat()
        print()

        tim_thay = True


if not tim_thay:
    print("Không có sách có vẽ bìa của tác giả này.")