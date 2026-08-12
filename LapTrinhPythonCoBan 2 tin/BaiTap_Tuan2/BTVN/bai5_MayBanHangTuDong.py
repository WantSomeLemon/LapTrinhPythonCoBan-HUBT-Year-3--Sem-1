choiceInput = 0
tongTien = 0
sl = None
while True:
    print("""========== MENU ĐỒ UỐNG ==========
    1. Nước suối       10.000
    2. Coca            15.000
    3. Cà phê          20.000
    4. Trà sữa         30.000
    5. Thoát
    ==================================""")
    choiceInput = int(input("Chọn số để tiếp tục chương trình: "))
    match choiceInput:
        case 1:
            name = "Nước suối"
            giaSP = 10000

        case 2:
            name = "Coca"
            giaSP = 15000
        case 3:
            name = "Cà phê"
            giaSP = 20000
        case 4:
            name = "Trà sữa"
            giaSP = 30000
        case 5:
            if tongTien >= 100000:
                print("Tổng tiền trước khi giảm giá: ", tongTien)
                print("Tổng tiền đã hơn 100k. Bạn được giảm giá 10% tổng đơn giá.")
                tongTien = tongTien - (tongTien * 0.1)
            print("Tổng số tiền bạn phải thanh toán: ", tongTien)
            print("Chào tạm biệt và không gặp lại!!")
            break
        case _:
            print("Số không hợp lệ, hãy chọn lại")
    sl = int(input("Nhập số lượng muốn mua: "))
    while sl <= 0:
        print("Số lượng không hợp lệ. Hãy nhập lại!!!")
        sl = int(input("Nhập số lượng muốn mua: "))
    thanhTien = giaSP * sl
    tongTien += thanhTien
    print("Tổng tiền hiện tại: ", tongTien)