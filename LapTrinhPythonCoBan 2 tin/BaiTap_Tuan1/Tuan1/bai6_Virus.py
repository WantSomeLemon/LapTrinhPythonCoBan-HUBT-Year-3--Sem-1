virus = int(input("Số lượng virus ban đầu: "))
muc_tieu = int(input("Số lượng cần vượt: "))

ngay = 0

while virus <= muc_tieu:
    virus *= 2
    ngay += 1

print("Sau", ngay, "ngày.")