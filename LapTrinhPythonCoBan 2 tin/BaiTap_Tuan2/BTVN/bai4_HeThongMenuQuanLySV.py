choiceInput = 0
name =""
classIn=""
dcn = None
dgk = None
dck = None
dtk = None
while True:
    print("""========== QUẢN LÝ SINH VIÊN ==========
    1. Nhập thông tin sinh viên
    2. Hiển thị thông tin
    3. Tính điểm trung bình
    4. Xếp loại
    5. Thoát
    ========================================""")

    choiceInput = int(input("Chọn số để tiếp tục chương trình: "))
    match choiceInput:
        case 1:
            name = input("Họ tên sinh viên: ")
            classIn = input("Lớp: ")
        case 2:
            if not name or not classIn:
                print("Chưa có thông tin sinh viên trong bộ nhớ. Hãy chọn 1 để nhập thông tin trước")
                continue
            print("Họ tên sinh viên: ", name)
            print("Lớp: ", classIn)
        case 3:
            dcn = float(input("Nhập điểm chuyên cần: "))
            while dcn < 0 or dcn > 10:
                dcn = float(input("Nhập lại điểm chuyên cần (trong khoảng 0 đến 10): "))

            dgk = float(input("Nhập điểm giữa kỳ: "))
            while dgk < 0 or dgk > 10:
                dgk = float(input("Nhập lại điểm giữa kỳ (trong khoảng 0 đến 10): "))

            dck = float(input("Nhập điểm cuối kì: "))
            while dck < 0 or dck > 10:
                dck = float(input("Nhập lại điểm cuối kì (trong khoảng 0 đến 10): "))

            dtk = 0.1 * dcn + 0.3 * dgk + 0.6 * dck
            print("Điểm tổng kết kì: ", dtk)
        case 4:
            if dtk is None:
                print("Chưa có điểm trung bình. Chọn số 3 để thực hiện.")
                continue
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

            print("Xếp loại: ", xepLoai)
            print(quaMon)
        case 5:
            print("Chào tạm biệt và không gặp lại!!")
            break
        case _:
            print("Số không hợp lệ, hãy chọn lại")

