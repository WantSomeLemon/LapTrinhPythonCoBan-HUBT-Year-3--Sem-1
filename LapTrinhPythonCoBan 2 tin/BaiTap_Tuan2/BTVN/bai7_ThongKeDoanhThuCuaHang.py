ds = []
tongTien = 0
n = int(input("Nhập số ngày: "))
while n <= 0:
    print("Số ngày không hợp lệ. Nhập lại")
    n = int(input("Nhập số ngày: "))

for i in range(1, n+1):
    tien = float(input(f"Nhập số doanh thu trong ngày {i}: "))
    while tien <= 0:
        print("Số doanh thu không hợp lệ. Nhập lại")
        tien = float(input(f"Nhập số doanh thu trong ngày {i}: "))
    trong_Ngay= [i,tien]
    ds.append(trong_Ngay)
    tongTien += tien
# Tinh trung binh
avgTien = tongTien / n

# max min
maxTien = minTien = ds[0][1]
ngayMax = ngayMin = ds[0][0]

for i in ds:
    if i[1] > maxTien:
        maxTien = i[1]
        ngayMax = i[0]

    if i[1] < minTien:
        minTien = i[1]
        ngayMin = i[0]



#so ngay tren trung binh
countDayMoreAvg = 0
countDayMoreThan10M = 0

for i in ds:
    if i[1] > avgTien:
        countDayMoreAvg += 1
    if i[1] > 10000000:
        countDayMoreThan10M += 1



print(f"""
--- KẾT QUẢ ---
Danh sách doanh thu: {ds}
Tổng doanh thu: {tongTien}
Doanh thu trung bình: {avgTien}
Ngày doanh thu cao nhất: Ngày {ngayMax} - Doanh thu: {maxTien}
Ngày doanh thu thấp nhất: Ngày {ngayMin} - Doanh thu: {minTien}
Số ngày doanh thu trên trung bình: {countDayMoreAvg}
Số ngày doanh thu > 10 triệu: {countDayMoreThan10M}
""")

