def in_so_nguyen_to(n):
    for i in range(2, n + 1):
        kt = True

        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                kt = False
                break

        if kt:
            print(i, end=" ")

n = int(input("Nhập n: "))
in_so_nguyen_to(n)