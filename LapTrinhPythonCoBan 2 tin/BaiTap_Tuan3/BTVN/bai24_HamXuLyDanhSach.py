def tinhTong(ds):
    tong = 0
    for so in ds:
        tong += so
    return tong

def timMax(ds):
    soLonNhat = ds[0]
    for so in ds:
        if so > soLonNhat:
            soLonNhat = so
    return soLonNhat

def timMin(ds):
    soNhoNhat = ds[0]
    for so in ds:
        if so < soNhoNhat:
            soNhoNhat = so
    return soNhoNhat

def demSoChan(ds):
    dem = 0
    for so in ds:
        if so % 2 == 0:
            dem += 1
    return dem

ds = [12, 5, 8, 21, 30, 17, 4, 9]
tong = tinhTong(ds)
soLonNhat = timMax(ds)
soNhoNhat = timMin(ds)
soChan = demSoChan(ds)

print(f"""
Danh sách: {ds}
Tổng: {tong}
Số lớn nhất: {soLonNhat}
Số nhỏ nhất: {soNhoNhat}
Số lượng số chẵn: {soChan}
""")