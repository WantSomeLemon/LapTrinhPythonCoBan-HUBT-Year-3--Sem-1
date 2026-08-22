st = input("Nhập một đoạn văn: ")

soKyTu = len(st)
soChuCai = 0
soChuSo = 0
soKhoangTrang = 0
soKyTuDacBiet = 0

for kyTu in st:
    if kyTu.isalpha():
        soChuCai += 1
    elif kyTu.isdigit():
        soChuSo += 1
    elif kyTu.isspace():
        soKhoangTrang += 1
    else:
        soKyTuDacBiet += 1

tach_tu = st.split()
soTu = len(tach_tu)

print("Số ký tự:", soKyTu)
print("Số chữ cái:", soChuCai)
print("Số chữ số:", soChuSo)
print("Số khoảng trắng:", soKhoangTrang)
print("Số ký tự đặc biệt:", soKyTuDacBiet)
print("Số từ:", soTu)