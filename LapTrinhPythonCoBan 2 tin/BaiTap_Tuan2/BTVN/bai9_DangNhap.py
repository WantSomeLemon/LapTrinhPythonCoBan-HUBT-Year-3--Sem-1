username_dung = "admin"
password_dung = "123456"

lan = 0

while lan < 3:
    username = input("Nhập username: ")
    password = input("Nhập password: ")

    if username == username_dung and password == password_dung:
        print("Đăng nhập thành công!")
        break
    else:
        lan += 1
        print("Đăng nhập sai!")

if lan == 3:
    print("Tài khoản đã bị khóa.")