import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

import pickle




def cau_2a_chia_du_lieu(dataset):

    # X: số năm kinh nghiệm
    X = dataset[
        "SoNamKinhNghiem"
    ].values.reshape(-1, 1)

    # y: mức lương
    y = dataset[
        "Luong"
    ].values.reshape(-1, 1)

    # Chia dữ liệu:
    # 80% dùng để huấn luyện
    # 20% dùng để kiểm thử
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=0
    )

    print("\n========== 2a. CHIA DỮ LIỆU ==========")

    print(
        "Số lượng dữ liệu huấn luyện:",
        len(X_train)
    )

    print(
        "Số lượng dữ liệu kiểm thử:",
        len(X_test)
    )

    return X_train, X_test, y_train, y_test


def cau_2b_huan_luyen_model(
    X_train,
    y_train
):

    # Khai báo mô hình Linear Regression
    model = LinearRegression()

    # Huấn luyện mô hình
    model.fit(
        X_train,
        y_train
    )

    print("\n========== 2b. HUẤN LUYỆN MODEL ==========")

    print(
        "Hệ số intercept:",
        model.intercept_
    )

    print(
        "Hệ số coefficient:",
        model.coef_
    )

    return model


def cau_2c_du_doan_luong(
    model,
    X_test
):

    # Sử dụng model để dự đoán
    y_pred = model.predict(
        X_test
    )

    print("\n========== 2c. DỰ ĐOÁN LƯƠNG ==========")

    print("Các giá trị lương dự đoán:")

    print(y_pred)

    return y_pred


def cau_2d_danh_gia_model(
    model,
    X_train,
    y_train,
    X_test,
    y_test,
    y_pred
):

    # Tính R2 trên tập huấn luyện
    r2_train = r2_score(
        y_train,
        model.predict(X_train)
    )

    # Tính R2 trên tập kiểm thử
    r2_test = r2_score(
        y_test,
        y_pred
    )

    # Tính MAE
    mae = mean_absolute_error(
        y_test,
        y_pred
    )

    print("\n========== 2d. ĐÁNH GIÁ MODEL ==========")

    print(
        "R2 trên tập huấn luyện:",
        r2_train
    )

    print(
        "R2 trên tập kiểm thử:",
        r2_test
    )

    print(
        "MAE:",
        mae
    )

    # Vẽ biểu đồ
    plt.figure(figsize=(8, 5))

    # Dữ liệu thực tế
    plt.scatter(
        X_test,
        y_test,
        label="Lương thực tế"
    )

    # Đường dự đoán
    plt.plot(
        X_test,
        y_pred,
        label="Lương dự đoán"
    )

    plt.title(
        "So sánh lương thực tế và lương dự đoán"
    )

    plt.xlabel(
        "Số năm kinh nghiệm"
    )

    plt.ylabel(
        "Lương"
    )

    plt.legend()

    plt.show()

def cau_2e_luu_model(model):

    filename = "model.sav"

    # Lưu model vào file
    pickle.dump(
        model,
        open(filename, "wb")
    )

    print("\n========== 2e. LƯU MODEL ==========")

    print(
        "Đã lưu model vào file:",
        filename
    )

def cau_2f_su_dung_model():

    filename = "model.sav"

    # Đọc model đã lưu
    loaded_model = pickle.load(
        open(filename, "rb")
    )

    print("\n========== 2f. SỬ DỤNG MODEL ==========")

    # Một số dữ liệu mới:
    # 1 năm, 2 năm và 4 năm kinh nghiệm
    X_moi = [
        [1],
        [2],
        [4]
    ]

    # Dự đoán
    y_moi = loaded_model.predict(
        X_moi
    )

    print(
        "Dự đoán lương:"
    )

    print(y_moi)




