n = int(input("Nhập n: "))

s1 = 2022

for i in range(1, n + 1):
    s1 += 2 * i

print("S =", s1)

#n = int(input("Nhập n: "))

s2 = 0
gt = 1

for i in range(1, n + 1):
    gt *= i      # gt = i!
    s2 += 1 / gt

print("S =", s2)

x = int(input("Nhập x: "))
y = int(input("Nhập y: "))

f = x**2 + y**2

print("Giá trị hàm =", f)