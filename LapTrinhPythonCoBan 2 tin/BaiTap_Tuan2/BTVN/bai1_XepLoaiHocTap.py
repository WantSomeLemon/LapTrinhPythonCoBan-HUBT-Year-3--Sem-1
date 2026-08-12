name = input("Nhập họ tên sinh viên: ")

dcn = float(input("Nhập điểm chuyên cần: "))
while dcn<0 or dcn>10:
    dcn = float(input("Nhập lại điểm chuyên cần (trong khoảng 0 đến 10): "))

dgk = float(input("Nhập điểm giữa kỳ: "))
while dgk<0 or dgk>10:
    dgk = float(input("Nhập lại điểm giữa kỳ (trong khoảng 0 đến 10): "))

dck =float(input("Nhập điểm cuối kì: "))
while dck<0 or dck>10:
    dck = float(input("Nhập lại điểm cuối kì (trong khoảng 0 đến 10): "))

dtk = 0.1*dcn + 0.3*dgk + 0.6*dck

# print(dcn, dgk, dck, dtk)

if 8.5 <= dtk <= 10:
    xepLoai = "Xuất sắc"
    quaMon = "Đạt"
elif 7.0 <= dtk < 8.5:
    xepLoai = "Giỏi"
    quaMon = "Đạt"
elif 5.5 <= dtk < 7.0:
    xepLoai = "Khá"
    quaMon = "Đạt"
elif 4.0 <= dtk < 5.5:
    xepLoai = "Trung bình"
    quaMon = "Đạt"
else:
    xepLoai = "Không cần nói nữa. Ở lại đây với a"
    quaMon = "Không đạt"

print("Điểm tổng kết: ", dtk)
print("Xếp loại: ",xepLoai)
print(quaMon)