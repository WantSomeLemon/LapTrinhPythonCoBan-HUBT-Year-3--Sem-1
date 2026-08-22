st = input("Nhập họ tên: ")

st = st.strip()
tach_tu = st.split()
so_tu = len(tach_tu)
ho = tach_tu[0]
ten = tach_tu[-1]
ten_dem = " ".join(tach_tu[1:-1])
viet_tat = ""

for tu in tach_tu:
    viet_tat += tu[0].upper()

print("Số từ:", so_tu)
print("Họ:", ho)
print("Tên đệm:", ten_dem)
print("Tên:", ten)
print("Viết tắt:", viet_tat)