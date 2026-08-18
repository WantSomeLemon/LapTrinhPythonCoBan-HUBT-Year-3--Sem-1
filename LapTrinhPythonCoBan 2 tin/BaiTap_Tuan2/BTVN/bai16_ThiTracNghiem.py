# tu tao dap an gia
dapAnDung = ["A", "B", "C", "D", "A", "B", "C", "D", "A", "B"]

soCauDung = 0
ketQua = []

for i in range(10):
    dapAn = input(f"Nhập đáp án câu {i + 1} (A/B/C/D): ").upper()

    while dapAn not in ["A", "B", "C", "D"]:
        print("Không hợp lệ, nhập lại")
        dapAn = input(f"Nhập đáp án câu {i + 1} (A/B/C/D): ").upper()

    if dapAn == dapAnDung[i]:
        soCauDung += 1
        ketQua.append(f"Câu {i + 1}: Đúng")
    else:
        ketQua.append(f"Câu {i + 1}: Sai")


# Tính điểm
diem = soCauDung


# Xếp loại
match soCauDung:
    case 9 | 10:
        xepLoai = "Xuất sắc"

    case 7 | 8:
        xepLoai = "Tốt"

    case 5 | 6:
        xepLoai = "Đạt"

    case _:
        xepLoai = "Không đạt"


print("""
--- KẾT QUẢ ---
""")

for kq in ketQua:
    print(kq)

print(f"""
--- THỐNG KÊ ---

Số câu đúng: {soCauDung}/10
Điểm: {diem}
Xếp loại: {xepLoai}
""")