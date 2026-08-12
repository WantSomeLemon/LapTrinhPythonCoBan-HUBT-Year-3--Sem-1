kw = int(input("Nhập số KW tiêu thụ: "))
while kw < 0:
    print("Lỗi!!! Số điên phải là số dương. Hãy nhập lại.")
    kw = int(input("Nhập số KW tiêu thụ: "))

if kw <= 50:
    tien = kw * 1800
elif kw <= 100:
    tien = 50 * 1800 + (kw - 50) * 2000
elif kw <= 200:
    tien = 50 * 1800 + 50 * 2000 + (kw - 100) * 2500
elif kw <= 300:
    tien = 50 * 1800 + 50 * 2000 + 100 * 2500 + (kw - 200) * 3000
else:
    tien = (
        50 * 1800 +
        50 * 2000 +
        100 * 2500 +
        100 * 3000 +
        (kw - 300) * 3500
    )

if  tien > 1000000:
    print("Mức tiêu thụ điện cao")
    print("Tiền điện phải trả:", tien, "VNĐ")
else:
    print("Tiền điện phải trả:", tien, "VNĐ")