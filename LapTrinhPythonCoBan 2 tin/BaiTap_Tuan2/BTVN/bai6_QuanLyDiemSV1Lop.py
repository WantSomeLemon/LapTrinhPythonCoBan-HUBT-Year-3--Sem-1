ds = []
n = int(input("Nhập số lượng sinh viên: "))
while n <= 0:
    print("Số lượng không hợp lệ. Nhập lại.")
    n = int(input("Nhập số lượng sinh viên: "))

# Nhập thông tin
for i in range(n):
    name = input("Họ tên: ")
    while not name:
        print("Tên không được để trống.")
        name = input("Họ tên: ")

    javaMark = float(input("Nhập điểm java: "))
    while javaMark < 0 or javaMark > 10:
        print("Điểm không hợp lệ. Nhập lại.")
        javaMark = float(input("Nhập điểm java: "))

    csdlMark = float(input("Nhập điểm CSDL: "))
    while csdlMark < 0 or csdlMark > 10:
        print("Điểm không hợp lệ. Nhập lại.")
        csdlMark = float(input("Nhập điểm CSDL: "))

    webMark = float(input("Nhập điểm Web: "))
    while webMark < 0 or webMark > 10:
        print("Điểm không hợp lệ. Nhập lại.")
        webMark = float(input("Nhập điểm Web: "))

    dtb = (javaMark + csdlMark + webMark) / 3

    if 8.5 <= dtb <= 10:
        xepLoai = "Xuất sắc"
        quaMon = "Đạt"
    elif 7.0 <= dtb < 8.5:
        xepLoai = "Giỏi"
        quaMon = "Đạt"
    elif 5.5 <= dtb < 7.0:
        xepLoai = "Khá"
        quaMon = "Đạt"
    elif 4.0 <= dtb < 5.5:
        xepLoai = "Trung bình"
        quaMon = "Đạt"
    else:
        xepLoai = "Yếu"
        quaMon = "Không đạt"

    sinhVien = [name, javaMark, csdlMark, webMark, round(dtb,2), xepLoai, quaMon]
    ds.append(sinhVien)

# print(ds)
'''
0: Name
1: Java Mark
2: CSDL Mark
3: Web Mark
4: Điểm trung bình
5: Xếp loại
6: Qua môn
'''

countPass = 0
countNotPass = 0
for i in ds:
    if i[6] == "Đạt":
        countPass += 1
    elif i[6] == "Không đạt":
        countNotPass += 1

dsDTB = [i[4] for i in ds]
dtbMax = max(dsDTB)
dtbMin = min(dsDTB)
dtbAVG = round(sum(dsDTB)/len(dsDTB), 2)

print(ds)

print(f"""========== THỐNG KÊ KẾT QUẢ ==========
• Số sinh viên đạt: {countPass}
• Số sinh viên không đạt: {countNotPass}
• Điểm trung bình cao nhất: {dtbAVG}
• Điểm trung bình thấp nhất: {dtbMin}
• Điểm trung bình của cả lớp: {dtbAVG}
===============================================""")