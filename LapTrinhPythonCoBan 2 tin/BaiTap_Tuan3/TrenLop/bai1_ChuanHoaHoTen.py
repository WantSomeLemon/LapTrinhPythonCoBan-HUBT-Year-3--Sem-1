st = input("Nhập họ tên: ")

st = st.strip()

#" ".join = chèn thêm dấu cách vào giữa các từ
tach_tu = st.split()
st = " ".join(tach_tu)

st = st.title()

print("Họ tên sau khi chuẩn hóa:", st)