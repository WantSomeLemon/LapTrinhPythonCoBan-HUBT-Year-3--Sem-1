'''
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

import pickle
'''

import pandas as pd
import cau2



dataset = pd.read_csv("../work_data.csv")

X_train, X_test, y_train, y_test = cau2.cau_2a_chia_du_lieu(dataset)

model = cau2.cau_2b_huan_luyen_model(
    X_train,
    y_train
)

y_pred = cau2.cau_2c_du_doan_luong(
        model,
        X_test
    )

cau2.cau_2d_danh_gia_model(
        model,
        X_train,
        y_train,
        X_test,
        y_test,
        y_pred
    )

cau2.cau_2e_luu_model(
        model
    )

cau2.cau_2f_su_dung_model()

