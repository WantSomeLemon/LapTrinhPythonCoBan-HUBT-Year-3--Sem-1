ds = []
tongTien = 0
n = int(input("Nhập số ngày: "))
while n <= 0:
    print("Số ngày không hợp lệ. Nhập lại")

for i in range(1, n+1):
    tien = float(input(f"Nhập số doanh thu trong ngày {i}: "))
    while tien <= 0:
        print("Số doanh thu không hợp lệ. Nhập lại")
        tien = float(input(f"Nhập số doanh thu trong ngày {i}: "))
    trong_Ngay= [i,tien]
    ds.append(trong_Ngay)
    tongTien += tien
print(ds)