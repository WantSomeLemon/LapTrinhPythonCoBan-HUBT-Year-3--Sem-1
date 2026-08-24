tuKhoaBai1 = {
    "python",
    "java",
    "database",
    "web",
    "sql"
}
tuKhoaBai2 = {
    "python",
    "sql",
    "html",
    "css",
    "web"
}

tuKhoaChung = tuKhoaBai1.intersection(tuKhoaBai2)
tuKhoaBai1Co = tuKhoaBai1.difference(tuKhoaBai2)
tuKhoaBai2Co = tuKhoaBai2.difference(tuKhoaBai1)
tatCaTuKhoa = tuKhoaBai1.union(tuKhoaBai2)

print(f"""
Từ khóa bài 1: {tuKhoaBai1}
Từ khóa bài 2: {tuKhoaBai2}
Từ khóa chung: {tuKhoaChung}
Từ khóa chỉ bài 1 có: {tuKhoaBai1Co}
Từ khóa chỉ bài 2 có: {tuKhoaBai2Co}
Tổng số từ khóa khác nhau: {len(tatCaTuKhoa)}
""")