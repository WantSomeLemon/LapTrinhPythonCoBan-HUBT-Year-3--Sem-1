class Vehicle:
    def __init__(self, giaTriXe, dungTich):
        self.giaTriXe = giaTriXe
        self.dungTich = dungTich

    def tinhThue(self):
        if self.dungTich < 100:
            return self.giaTriXe * 0.01
        elif 100 <= self.dungTich <= 200:
            return self.giaTriXe * 0.03
        else:
            return self.giaTriXe * 0.05

    def xuatThongTin(self):
        print(f"Trị giá xe: {self.giaTriXe:,.0f} VNĐ |"
              f" Dung tích: {self.dungTich}cc |"
              f" Thuế trước bạ: {self.tinhThue():,.0f} VNĐ")

# Console
print("\n--- NHẬP THÔNG TIN XE ---")
xe1 = Vehicle(float(input("Trị giá xe 1: ")),
              int(input("Dung tích xe 1 (cc): ")))
xe2 = Vehicle(float(input("Trị giá xe 2: ")),
              int(input("Dung tích xe 2 (cc): ")))
xe3 = Vehicle(float(input("Trị giá xe 3: ")),
              int(input("Dung tích xe 3 (cc): ")))

print("\n--- KÊ KHAI THUẾ TRƯỚC BẠ ---")
print("Xe 1: ", end=""); xe1.xuatThongTin()
print("Xe 2: ", end=""); xe2.xuatThongTin()
print("Xe 3: ", end=""); xe3.xuatThongTin()