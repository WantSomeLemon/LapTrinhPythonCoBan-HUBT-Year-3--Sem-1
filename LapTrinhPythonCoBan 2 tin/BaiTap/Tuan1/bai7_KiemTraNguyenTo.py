import math

n = int(input("Nhập n: "))

if n < 2:
    print("NO")
else:
    check = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            check = False
            break

    if check:
        print("YES")
    else:
        print("NO")