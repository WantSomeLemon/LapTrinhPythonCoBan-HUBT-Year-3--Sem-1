ds = [1, 2, 3, 2, 4, 5, 3, 6, 1]
dsKhongTrung = []

for so in ds:
    if so not in dsKhongTrung:
        dsKhongTrung.append(so)
print(f"""
Danh sách ban đầu: {ds}
Danh sách không trùng: {dsKhongTrung}
""")