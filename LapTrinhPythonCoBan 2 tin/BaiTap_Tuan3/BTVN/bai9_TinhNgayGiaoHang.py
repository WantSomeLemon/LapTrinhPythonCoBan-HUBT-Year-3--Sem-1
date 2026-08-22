from datetime import datetime, timedelta

ngayDatHang = input("Nhập ngày đặt hàng (dd/mm/yyyy): ")
soNgayGiao = int(input("Nhập số ngày giao: "))

ngayDatHang = datetime.strptime(ngayDatHang, "%d/%m/%Y")
ngayNhan = ngayDatHang
demNgay = 0

while demNgay < soNgayGiao:
    ngayNhan += timedelta(days=1)
    if ngayNhan.weekday() != 5 and ngayNhan.weekday() != 6:
        demNgay += 1
print("Ngày nhận dự kiến:", ngayNhan.strftime("%d/%m/%Y"))