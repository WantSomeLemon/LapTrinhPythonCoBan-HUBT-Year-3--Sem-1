import pandas as pd

def cau_1a_doc_du_lieu():
    dataset = pd.read_csv("../work_data.csv")

    print("\n========== 1a. ĐỌC DỮ LIỆU TỪ FILE CSV ==========")
    print(dataset)

    return dataset

def cau_1b_hien_thi_hang_dau(dataset):
    print("\n========== 1b. CÁC HÀNG ĐẦU TIÊN ==========")
    print(dataset.head(10))

def cau_1c_hien_thi_hang_cuoi(dataset):
    print("\n========== 1c. CÁC HÀNG CUỐI CÙNG ==========")
    print(dataset.tail(10))

def cau_1d_xem_thong_tin(dataset):
    print("\n========== 1d. THÔNG TIN CƠ BẢN ==========")
    dataset.info()

def cau_1e_kiem_tra_gia_tri_thieu(dataset):
    print("\n========== 1e. GIÁ TRỊ THIẾU ==========")

    print("Số giá trị thiếu của từng cột:")
    print(dataset.isnull().sum())

    print("\nTổng số giá trị thiếu:")
    print(dataset.isnull().sum().sum())


def cau_1f_ket_cau_theo_nganh(dataset):
    print("\n========== 1f. KẾT CẤU DỮ LIỆU THEO NGÀNH ==========")

    print(dataset["NganhNghe"].value_counts())

    df_ke_toan = dataset[
        dataset["NganhNghe"] == "KeToan"
    ]

    df_sale = dataset[
        dataset["NganhNghe"] == "Sale"
    ]

    df_hcns = dataset[
        dataset["NganhNghe"] == "HCNS"
    ]

    print("\nChi tiết từng ngành:")

    print("KeToan:", df_ke_toan.shape[0], "mẫu")
    print("Sale:", df_sale.shape[0], "mẫu")
    print("HCNS:", df_hcns.shape[0], "mẫu")
