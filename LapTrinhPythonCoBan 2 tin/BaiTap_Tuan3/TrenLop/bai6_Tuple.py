hoa = (
    "Hoa Hồng",
    "Hoa Lan",
    "Hoa Cúc",
    "Hoa Mai",
    "Hoa Đào",
    "Hoa Sen",
    "Hoa Ly",
    "Hoa Giấy",
    "Hoa Sứ"
)

F1 = hoa[:4]
F2 = hoa[4:]

print("F1 =", F1)
print("F2 =", F2)

print("Độ dài tên trong F1")
for i in F1:
    print(i, ":", len(i))

print("Độ dài tên trong F2")
for i in F2:
    print(i, ":", len(i))