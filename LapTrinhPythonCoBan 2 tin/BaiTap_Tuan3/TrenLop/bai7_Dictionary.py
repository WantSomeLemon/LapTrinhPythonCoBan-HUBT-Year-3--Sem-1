students = [
    {"ma": "SV01", "ten": "Bach", "tuoi": 20, "thanhpho": "Ha Noi"},
    {"ma": "SV02", "ten": "VinhAnh", "tuoi": 18, "thanhpho": "Hai Phong"},
    {"ma": "SV03", "ten": "Minh Hung", "tuoi": 21, "thanhpho": "Lao Cai"},
    {"ma": "SV04", "ten": "Tuan", "tuoi": 19, "thanhpho": "Thanh Hoa"}
]

print("Danh sách sinh viên")
for sv in students:
    print(sv)

print("Sinh viên từ 20 tuổi trở lên")
for sv in students:
    if sv["tuoi"] >= 20:
        print(sv)

print("Sinh viên ở Hà Nội")
for sv in students:
    if sv["thanhpho"] == "Ha Noi":
        print(sv)