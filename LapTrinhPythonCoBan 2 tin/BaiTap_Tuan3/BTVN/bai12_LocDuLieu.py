ds = [12, 5, 8, 21, 30, 17, 4, 9]
soChan = []
soLe = []
soLonHon10 = []
soNguyenTo = []

for so in ds:
    if so % 2 == 0:
        soChan.append(so)
    else:
        soLe.append(so)
    if so > 10:
        soLonHon10.append(so)
    demUoc = 0
    for i in range(1, so + 1):
        if so % i == 0:
            demUoc += 1
    if demUoc == 2:
        soNguyenTo.append(so)

print(f"""
Danh sách ban đầu: {ds}
Số chẵn: {soChan}
Số lẻ: {soLe}
Số lớn hơn 10: {soLonHon10}
Số nguyên tố: {soNguyenTo}
""")