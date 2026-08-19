st = input("Nhập chuỗi: ")

print("Số ký tự: ", len(st))

str_split = st.split()
print("Số từ:", len(str_split))

print("Mỗi từ trên một dòng:")
for i in str_split:
    print(i)

print("Chuẩn hóa:")
for i in str_split:
    print(i.title())

ket_qua = " ".join(str_split)

print("Chuỗi sau khi nối (chuỗi ban đầu):", ket_qua)