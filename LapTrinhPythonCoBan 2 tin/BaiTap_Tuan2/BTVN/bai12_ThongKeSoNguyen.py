n = int(input("Nhập n: "))
while n <0:
    print("Âm số thứ tự ?")
    n = int(input("Nhập n: "))

sumPositiveNum = 0
evenCount = 0
oddCount = 0

for i in range(n):
    so = int(input(f"Nhập số thứ {i + 1}: "))

    # Gặp số 0 thì dừng chương trình
    if so == 0:
        break

    # Bỏ qua số âm
    if so < 0:
        continue

    # Tính tổng các số dương
    sumPositiveNum += so

    # Đếm số chẵn và số lẻ
    if so % 2 == 0:
        evenCount += 1
    else:
        oddCount += 1

print("Tổng các số dương:", sumPositiveNum)
print("Số lượng số chẵn:", evenCount)
print("Số lượng số lẻ:", oddCount)