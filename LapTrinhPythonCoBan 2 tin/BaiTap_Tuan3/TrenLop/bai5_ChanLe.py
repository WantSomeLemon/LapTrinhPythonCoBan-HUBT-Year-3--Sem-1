n = int(input("Nhập số phần tử: "))

ds = []

for i in range(n):
    x = int(input("Nhập phần tử: "))
    ds.append(x)

tong_chan = 0
tong_le = 0

print("Các số chẵn:")
for i in ds:
    if i % 2 == 0:
        print(i, end=" ")
        tong_chan += i

print()

print("Các số lẻ:")
for i in ds:
    if i % 2 != 0:
        print(i, end=" ")
        tong_le += i



print("Tổng chẵn:", tong_chan)
print("Tổng lẻ:", tong_le)