st = input("Nhập đoạn văn: ")
tuCanTim = input("Nhập từ cần tìm: ")

st = st.lower()
tuCanTim = tuCanTim.lower()
tach_tu = st.split()
dem = 0

for tu in tach_tu:
    if tu == tuCanTim:
        dem += 1
if dem > 0:
    print("Từ cần tìm có xuất hiện.")
    print("Số lần xuất hiện:", dem)
else:
    print("Từ cần tìm không xuất hiện.")