import math

A = (3, 4)
B = (7, 8)
x1 = A[0]
y1 = A[1]
x2 = B[0]
y2 = B[1]

khoangCach = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"""
Tọa độ A: {A}
Tọa độ B: {B}
Khoảng cách giữa A và B: {khoangCach}
""")