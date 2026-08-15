P = float(input("Nhập số tiền ban đầu P: "))
while P < 0:
    print("Nghèo? Sao lại âm tiền")
    P = float(input("Nhập số tiền ban đầu P: "))
n = int(input("Nhập số năm gửi: "))
while n < 0:
    print("Người âm à? Sao lại âm năm")
    n = int(input("Nhập số năm gửi: "))

print("""\nChọn hình thức tính lãi: 
1. Lãi đơn
2. Lãi kép""")

lua_chon = int(input("Nhập lựa chọn (1/2): "))
while lua_chon < 1 or lua_chon > 2:
    print("Chọn 1 hoặc 2 thôi.")
    lua_chon = int(input("Nhập lựa chọn (1/2): "))

lai_suat = 0.06

match lua_chon:
    case 1:
        print("--- LÃI ĐƠN ---")
        for nam in range(1, n + 1):
            tien = P * (1 + lai_suat * nam)
            print(f"Năm {nam}: {tien:,.2f}")

    case 2:
        print("--- LÃI KÉP ---")
        for nam in range(1, n + 1):
            tien = P * (1 + lai_suat) ** nam
            print(f"Năm {nam}: {tien:,.2f}")

    case _:
        print("Lựa chọn không hợp lệ!")