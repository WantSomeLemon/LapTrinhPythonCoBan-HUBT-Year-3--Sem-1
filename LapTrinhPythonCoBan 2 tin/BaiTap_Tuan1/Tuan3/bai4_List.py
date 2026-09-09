ds = []

while True:
    x = float(input("Nhập số (0 để dừng): "))

    if x == 0:
        break

    ds.append(x)

print("Danh sách vừa nhập:")
print(ds)