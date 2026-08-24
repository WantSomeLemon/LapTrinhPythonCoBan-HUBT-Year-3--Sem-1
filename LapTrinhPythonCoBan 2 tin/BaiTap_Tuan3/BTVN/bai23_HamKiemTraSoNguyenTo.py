def laSoNguyenTo(n):
    demUoc = 0
    for i in range(1, n + 1):
        if n % i == 0:
            demUoc += 1
    if demUoc == 2:
        return True
    else:
        return False

n = int(input("Nhập số nguyên: "))
if laSoNguyenTo(n):
    print(f"{n} là số nguyên tố.")
else:
    print(f"{n} không phải là số nguyên tố.")