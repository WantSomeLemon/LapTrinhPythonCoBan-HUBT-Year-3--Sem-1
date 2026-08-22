from datetime import datetime, timedelta

ngayBatDau = input("Nhập ngày bắt đầu khóa học (dd/mm/yyyy): ")
ngayBatDau = datetime.strptime(ngayBatDau, "%d/%m/%Y")
lichHoc = [
    "Tiếng Anh",
    "Nghỉ",
    "Lập trình cơ bản Python",
    "Tin4",
    "Tiếng Anh",
    "Lập trình cơ sở dữ liệu phân tán",
    "Tin4"
]

ngayHienTai = ngayBatDau
soBuoi = 0

while soBuoi < 48:
    thu = ngayHienTai.weekday()
    if lichHoc[thu] != "Nghỉ":
        print(
            ngayHienTai.strftime("%d/%m/%Y"),
            "-",
            lichHoc[thu]
        )
        soBuoi += 1
    ngayHienTai += timedelta(days=1)
ngayKetThuc = ngayHienTai - timedelta(days=1)

print("Ngày bắt đầu:", ngayBatDau.strftime("%d/%m/%Y"))
print("Ngày kết thúc:", ngayKetThuc.strftime("%d/%m/%Y"))
print("Số buổi học:", soBuoi)
print("Ngày học cuối cùng:", ngayKetThuc.strftime("%d/%m/%Y"))