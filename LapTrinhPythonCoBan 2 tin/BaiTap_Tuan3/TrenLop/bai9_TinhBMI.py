def tinh_bmi(weight, height):
    bmi = weight / (height ** 2)

    print("BMI =", round(bmi, 2))

    if bmi < 18.5:
        print("Gầy")

    elif bmi < 25:
        print("Bình thường")

    elif bmi < 30:
        print("Thừa cân")

    else:
        print("Béo phì")


weight = float(input("Nhập cân nặng (kg): "))
height = float(input("Nhập chiều cao (m): "))

tinh_bmi(weight, height)