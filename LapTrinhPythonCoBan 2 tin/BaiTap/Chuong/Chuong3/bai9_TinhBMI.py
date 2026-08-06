def tinh_bmi(can_nang, chieu_cao):
    bmi = can_nang / (chieu_cao ** 2)

    print("BMI =", round(bmi, 2))

    if bmi < 18.5:
        print("Gầy")

    elif bmi < 25:
        print("Bình thường")

    elif bmi < 30:
        print("Thừa cân")

    else:
        print("Béo phì")


can_nang = float(input("Nhập cân nặng (kg): "))
chieu_cao = float(input("Nhập chiều cao (m): "))

tinh_bmi(can_nang, chieu_cao)