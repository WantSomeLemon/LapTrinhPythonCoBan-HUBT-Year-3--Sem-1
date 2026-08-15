n = int(input("Nhập số sinh viên: "))
while n <= 0:
    print("Trường ma ?")
    n = int(input("Nhập số sinh viên: "))

for i in range(1, n + 1):
    diem = float(input(f"Nhập điểm sinh viên {i}: "))
    while diem < 0:
        print("Âm điểm?")
        diem = float(input(f"Nhập điểm sinh viên {i}: "))

    if diem >= 8.5:
        print(f"Sinh viên đầu tiên đạt học bổng là sinh viên {i}")
        print(f"Điểm: {diem}")
        break
else:
    print("Không có sinh viên nào đạt học bổng.")