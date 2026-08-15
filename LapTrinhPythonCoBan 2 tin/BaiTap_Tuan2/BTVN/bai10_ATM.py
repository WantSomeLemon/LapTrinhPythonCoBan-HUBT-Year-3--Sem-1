moneyBank = 10000000


while True:
    print("""===== ATM =====
    1. Xem số dư
    2. Rút tiền
    3. Nạp tiền
    4. Đổi mã PIN
    5. Thoát""")

    choicee = int(input("Nhập lựa chọn: "))
    while choicee < 1 or choicee > 5:
        print("Chọn từ 1 đến 5")
        choicee = int(input("Nhập lựa chọn: "))

    match choicee:
        case 1:
            print("Số dư hiện tại:", moneyBank, "đồng")

        case 2:
            moneyWithdraw = int(input("Nhập số tiền muốn rút: "))

            if moneyWithdraw <= 0:
                print("Số tiền rút phải lớn hơn 0!")
            elif moneyWithdraw > moneyBank:
                print("Không được rút quá số dư!")
            elif moneyWithdraw % 50000 != 0:
                print("Số tiền rút phải là bội số của 50.000!")
            else:
                moneyBank -= moneyWithdraw
                print("Rút tiền thành công!")
                print("Số dư còn lại:", moneyBank, "đồng")

        case 3:
            moneyAdd = int(input("Nhập số tiền muốn nạp: "))

            if moneyAdd <= 0:
                print("Số tiền nạp phải lớn hơn 0!")
            else:
                moneyBank += moneyAdd
                print("Nạp tiền thành công!")
                print("Số dư hiện tại:", moneyBank, "đồng")

        case 4:
            print("Chức năng đổi mã PIN.")

        case 5:
            print("Cảm ơn bạn đã sử dụng ATM!")
            break

        case _:
            print("Lựa chọn không hợp lệ!")