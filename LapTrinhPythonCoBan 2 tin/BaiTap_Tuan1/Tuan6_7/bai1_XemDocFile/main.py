'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

nhớ import các thư viện trên (có khả năng phải tải)
'''

import cau1
import cau2
import cau3


# 1. Xem thông tin dữ liệu


dataset = cau1.cau_1a_doc_du_lieu()

cau1.cau_1b_hien_thi_hang_dau(dataset)

cau1.cau_1c_hien_thi_hang_cuoi(dataset)

cau1.cau_1d_xem_thong_tin(dataset)

cau1.cau_1e_kiem_tra_gia_tri_thieu(dataset)

cau1.cau_1f_ket_cau_theo_nganh(dataset)


# 2. Phân tích dữ liệu


cau2.cau_2a_thong_ke_luong_theo_nganh(dataset)

cau2.cau_2b_thong_ke_luong_theo_kinh_nghiem(dataset)

cau2.cau_2c_luong_binh_quan_theo_nganh(dataset)


# 3. Trực quan hóa


cau3.cau_3a_histplot_luong(dataset)

cau3.cau_3b_boxplot_luong_theo_nganh(dataset)

cau3.cau_3c_scatter_kinh_nghiem_luong(dataset)

cau3.cau_3d_bar_luong_trung_binh_theo_nganh(dataset)

cau3.cau_3e_bar_luong_binh_quan(dataset)
