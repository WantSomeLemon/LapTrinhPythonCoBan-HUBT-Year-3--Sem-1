name = input("Nhập tên sinh viên: ")
stc = int(input("Nhập số tín chỉ: "))
while stc <= 0:
    print("Số tín chỉ phải > 0. Hãy nhập lại")
    stc = int(input("Nhập số tín chỉ: "))

studentTypes = ["chinhquy", "cao", "quocte"]
studentInput = input("Chọn 1 trong 3 loại (chinhquy, cao, quocte): ").strip().lower()

while studentInput not in studentTypes:
    print("Chỉ được chọn 1 trong 3 loại (chinhquy, cao, quocte)")
    studentInput = input("Loại sinh viên: ").strip().lower()

# print(studentInput)

if studentInput == "chinhquy":
    hp = 450000 * stc
elif studentInput == "cao":
    hp = 750000 * stc
elif studentInput == "quocte":
    hp = 1200000 * stc

# print(hp)

if stc >= 20:
    hp = hp - (hp * 0.05)

print("Số tiền phải đóng là: ", hp)

