st = input("Nhập chuỗi: ")
tachTu = st.lower().split()
demTu = {}

for tu in tachTu:
    if tu in demTu:
        demTu[tu] += 1
    else:
        demTu[tu] = 1

print(f"""
Chuỗi ban đầu: {st}
Số lần xuất hiện của các từ: {demTu}
""")