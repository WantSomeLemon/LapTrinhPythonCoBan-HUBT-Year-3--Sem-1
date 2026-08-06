st = input("Nhập họ tên: ")

#strip = xóa 2 bên
st = st.strip()

#split = tách thành 1 list substr có các từ
#" ".join = chèn thêm dấu cách vào giữa các từ
st = " ".join(st.split())

#Viết hoa chữ cái đầu
st = st.title()

print("Họ tên sau khi chuẩn hóa:", st)