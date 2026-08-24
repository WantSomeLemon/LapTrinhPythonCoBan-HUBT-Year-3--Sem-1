import re

def chuanHoaHoTen(hoTen):
    hoTen = hoTen.strip()
    tachTu = hoTen.split()
    hoTen = " ".join(tachTu)
    hoTen = hoTen.title()
    return hoTen

def demTu(st):
    tachTu = st.split()
    return len(tachTu)

def demNguyenAm(st):
    dem = 0
    for kyTu in st.lower():
        if kyTu in "aeiou":
            dem += 1
    return dem

def kiemTraEmail(email):
    mau = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    if re.match(mau, email):
        return True
    else:
        return False

hoTen = input("Nhập họ tên: ")
st = input("Nhập chuỗi: ")
email = input("Nhập email: ")
hoTenChuanHoa = chuanHoaHoTen(hoTen)
soTu = demTu(st)
soNguyenAm = demNguyenAm(st)
emailHopLe = kiemTraEmail(email)

print(f"""
Họ tên sau khi chuẩn hóa: {hoTenChuanHoa}
Số từ: {soTu}
Số nguyên âm: {soNguyenAm}
Email hợp lệ: {emailHopLe}
""")