class SOHOC:

    def __init__(self):
        self.number1 = 0
        self.number2 = 0

    def inputInfo(self):
        self.number1 = float(input("Nhập số thứ nhất: "))
        self.number2 = float(input("Nhập số thứ hai: "))

    def printInfo(self):
        print("Số thứ nhất:", self.number1)
        print("Số thứ hai:", self.number2)

    def addition(self):
        print("Tổng =", self.number1 + self.number2)

    def substract(self):
        print("Hiệu =", self.number1 - self.number2)

    def multi(self):
        print("Tích =", self.number1 * self.number2)

    def division(self):
        if self.number2 == 0:
            print("Không thể chia cho 0")
        else:
            print("Thương =", self.number1 / self.number2)