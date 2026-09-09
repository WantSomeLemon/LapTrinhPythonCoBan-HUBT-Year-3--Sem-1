from itertools import product

ten = input("Nhập tên người rút: ")
so_du = int(input("Nhập số tiền trong tài khoản: "))

while True:
    rut = int(input("Nhập số tiền muốn rút (bội số 50K): "))

    if rut > so_du:
        print("Không đủ tiền!")
        continue

    if rut % 50000 != 0:
        print("Số tiền này không phải là bội số của 50k! Hãy thực hiện lại chương trình")
        continue

    print("\nCác phương án rút tiền:")

    dem = 0

    for a in range(rut // 500000 + 1):
        for b in range(rut // 200000 + 1):
            for c in range(rut // 100000 + 1):
                for d in range(rut // 50000 + 1):
                    if a * 500000 + b * 200000 + c * 100000 + d * 50000 == rut:
                        dem += 1
                        print(
                            f"{dem}: "
                            f"500k={a}, "
                            f"200k={b}, "
                            f"100k={c}, "
                            f"50k={d}"
                        )

    print("\nTổng số phương án:", dem)

    so_du -= rut

    print("\nThông tin")
    print("Người rút:", ten)
    print("Đã rút:", rut)
    print("Số dư còn lại:", so_du)

    tiep = input("\nRút tiếp? (Y/N): ").upper()

    if tiep != "Y":
        break