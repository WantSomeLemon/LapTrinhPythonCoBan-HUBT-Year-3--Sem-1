import pandas as pd # Khai báo thư viện hỗ trợ đọc và phân tích dữ liệu ở dạng bảng
dataset = pd.read_csv("work_data.csv") # Lấy dữ liệu từ file work_data.csv đê phân tích và đặt tên dữ liệu đó là dataset
dataset.head(10) # xem 6 dòng đầu tiên của bảng dữ liệu
dataset.shape[1] # số lượng quan sát
dataset.describe()
df_keToan = dataset[dataset["NganhNghe"] == "KeToan"]
df_hcnh = dataset[dataset["NganhNghe"] == "HCNS"]
df_sale = dataset[dataset["NganhNghe"] == "Sale"]
import matplotlib.pyplot as plt  # Khai báo thư viện để vẽ hình
def bieu_do_luong_kinhnghiem():
    dataset.plot(x='SoNamKinhNghiem', y='Luong', style='o')
    plt.title('số năm kinh nghiệm - lương')
    plt.xlabel('số năm kinh nghiệm')
    plt.ylabel('lương')
    plt.show()
def bieu_do_histogram():
    # vẽ biểu đồ histogram
    plt.hist(dataset['Luong'], 20)
    plt.show()
def bieu_do_phan_bo_luongKT():
    plt.boxplot(df_keToan['Luong'])
    plt.show()
def show_bo_dl():
    print("Kết cấu bộ dữ liệu")
    print("Số lượng mẫu nhân viên kế toán: " + str(df_keToan.shape[0]))
    print("Số lượng mẫu nhân viên HCNH: " + str(df_hcnh.shape[0]))
    print("Số lượng mẫu nhân viên SALE: " + str(df_sale.shape[0]))
def dudoan_():
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    X=dataset['SoNamKinhNghiem'].values.reshape(-1,1)
    y=dataset['Luong'].values.reshape(-1,1)
    # chia bộ dữ liệu ra 2 tập train và test theo tỷ lệ 80% train, 20% test
    X_traint, X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)
    regressor=LinearRegression()#khai báo mô hình tuyến tính
    regressor.fit(X_traint,y_train)#huấn luyện mô hình
    print("Mô hình hồi quy sẽ có dạng: Lương=a+b*sonamkinhnghiem:")
    print(regressor.intercept_)
    print(regressor.coef_)
    # Đánh giá độ chính xác của mô hình
    y_pred=regressor.predict(X_test)#dự đoán trên số năm kinh nghiệm của bộ dữ liệu test
    import sklearn.metrics as metrics
    from sklearn.metrics import r2_score
    r2_test=r2_score(y_test,y_pred)
    print('R2 trên tập kiểm tra model là:' + str(r2_test))
    r2_train=r2_score(y_train,regressor.predict(X_traint))
    print('R2 trên tập huấn luyện model là:'+str(r2_train))
    # Đánh giá bằng mô hình
    plt.scatter(X_test,y_test,color='red')
    plt.plot(X_test,y_pred,color='blue')
    plt.show()
    plt.scatter(X_test,y_test)
while True:
    print('''**********************
    1. Vẽ biểu đồ Số năm kinh nghiệm và lương
    2. Vẽ biểu đồ histogram
    3. Biểu dồ phân bố lương nhân viên kế toán
    4. Show bộ dữ liệu
    0. Thoát chương trình
    *****************''')
    chon=int(input(" Ban hay chon lua chon: "))
    if chon==1:
        bieu_do_luong_kinhnghiem()
    if chon==2:
        bieu_do_histogram()
    if chon==3:
        bieu_do_phan_bo_luongKT()
    if chon==4:
        show_bo_dl()
    if chon==5:
        dudoan_()
    if chon==0:
        break