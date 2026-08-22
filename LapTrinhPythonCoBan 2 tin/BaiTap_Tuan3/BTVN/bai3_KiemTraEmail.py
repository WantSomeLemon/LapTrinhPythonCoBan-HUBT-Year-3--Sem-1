import re

# Dung regex
email = input("Nhập email: ")
mau = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
if re.match(mau, email):
    print("Email hợp lệ.")
else:
    print("Email không hợp lệ.")