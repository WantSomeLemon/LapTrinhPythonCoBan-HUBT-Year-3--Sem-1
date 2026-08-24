lop_a = {"SV01", "SV02", "SV03", "SV04"}
lop_b = {"SV03", "SV04", "SV05", "SV06"}

sinhVienCaHai = lop_a.intersection(lop_b)
sinhVienLopA = lop_a.difference(lop_b)
sinhVienLopB = lop_b.difference(lop_a)
tatCaSinhVien = lop_a.union(lop_b)

print(f"""
Lớp A: {lop_a}
Lớp B: {lop_b}
Sinh viên cả hai lớp: {sinhVienCaHai}
Sinh viên chỉ thuộc lớp A: {sinhVienLopA}
Sinh viên chỉ thuộc lớp B: {sinhVienLopB}
Tất cả sinh viên: {tatCaSinhVien}
""")