import models

ds_KySu = []

n = int(input("Nhập số lượng kỹ sư:"))

#Nhap ds
for i in range(n):
    print(f"\n--- Nhập kỹ sư thứ {i + 1} ---")
    ky_su = models.KySu()
    ky_su.nhap()
    ds_KySu.append(ky_su)

#In ds
#dung enumerate thay cho range(lenght), vi cai nay la cua python moi co nen nghich thu
for i, ky_su in enumerate(ds_KySu, 1):
    print(f"\n--- Kỹ sư {i} ---")
    ky_su.xuat()

#Tim nam tot nghiep gan day
if len(ds_KySu) > 0:
    nam_max = max(ky_su.nam_tot_nghiep for ky_su in ds_KySu)

    print("\n========== KỸ SƯ TỐT NGHIỆP GẦN ĐÂY NHẤT ==========")

    for ky_su in ds_KySu:
        if ky_su.nam_tot_nghiep == nam_max:
            ky_su.xuat()
            print()

