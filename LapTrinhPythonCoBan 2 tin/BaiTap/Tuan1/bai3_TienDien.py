kw = int(input("Nhập số KW tiêu thụ: "))

if kw <= 50:
    tien = kw * 1678
elif kw <= 100:
    tien = 50 * 1678 + (kw - 50) * 1734
elif kw <= 200:
    tien = 50 * 1678 + 50 * 1734 + (kw - 100) * 2014
elif kw <= 300:
    tien = 50 * 1678 + 50 * 1734 + 100 * 2014 + (kw - 200) * 2536
elif kw <= 400:
    tien = 50 * 1678 + 50 * 1734 + 100 * 2014 + 100 * 2536 + (kw - 300) * 2834
else:
    tien = (
        50 * 1678 +
        50 * 1734 +
        100 * 2014 +
        100 * 2536 +
        100 * 2834 +
        (kw - 400) * 2927
    )

print("Tiền điện phải trả:", tien, "VNĐ")