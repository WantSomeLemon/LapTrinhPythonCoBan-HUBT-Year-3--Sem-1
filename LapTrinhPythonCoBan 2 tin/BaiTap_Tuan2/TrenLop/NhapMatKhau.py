password=input("Pass: ")
dem=1
while password != "abcd1234":
    dem +=1
    password=input("Nhập lại pass: ")
    if dem == 5:
        print("Khoá thẻ")
        break
else:
    print("Thành công")