diem = [7.5, 8, 6.5, 9, 5.5, 8.5]
tong = 0
demDat = 0

for d in diem:
    tong += d
    if d >= 5:
        demDat += 1

trungBinh = tong / len(diem)
diemCaoNhat = diem[0]
diemThapNhat = diem[0]

for d in diem:
    if d > diemCaoNhat:
        diemCaoNhat = d
    if d < diemThapNhat:
        diemThapNhat = d

diemTangDan = sorted(diem)
diemGiamDan = sorted(diem, reverse=True)

print(f"""
Tổng điểm: {tong}
Điểm trung bình: {trungBinh:.2f}
Điểm cao nhất: {diemCaoNhat}
Điểm thấp nhất: {diemThapNhat}
Số sinh viên đạt: {demDat}
Điểm tăng dần: {diemTangDan}
Điểm giảm dần: {diemGiamDan}
""")