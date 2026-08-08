import numpy as np



# ============================================================
# PHẦN 1: BÀI TẬP VỀ NUMPY
# ============================================================

# Bài 1: Tạo một array gồm 10 số 0
def bai_1():
    a = np.zeros(10)

    print("\n========== BÀI 1 ==========")
    print(a)

# Bài 2: Tạo một array gồm 10 số 1
def bai_2():
    a = np.ones(10)

    print("\n========== BÀI 2 ==========")
    print(a)

# Bài 3: Tạo một array gồm 10 số 5

def bai_3():
    a = np.full(10, 5)

    print("\n========== BÀI 3 ==========")
    print(a)

# Bài 4: Tạo array gồm các số nguyên từ 10 đến 50
def bai_4():
    a = np.arange(10, 51)

    print("\n========== BÀI 4 ==========")
    print(a)

# Bài 5: Tạo array gồm các số chẵn từ 10 đến 50
def bai_5():
    a = np.arange(10, 51, 2)

    print("\n========== BÀI 5 ==========")
    print(a)

# Bài 6: Tạo ma trận 3x3 có giá trị từ 0 đến 8

def bai_6():
    a = np.arange(9).reshape(3, 3)

    print("\n========== BÀI 6 ==========")
    print(a)

# Bài 7: Tạo ma trận đơn vị 3x3
def bai_7():
    a = np.eye(3)

    print("\n========== BÀI 7 ==========")
    print(a)


# Bài 8: Tạo một số ngẫu nhiên từ 0 đến 1
def bai_8():
    a = np.random.rand(1)

    print("\n========== BÀI 8 ==========")
    print(a)

# Bài 9: Tạo array gồm 25 số ngẫu nhiên
# theo phân phối chuẩn
def bai_9():
    a = np.random.randn(25)

    print("\n========== BÀI 9 ==========")
    print(a)

# Bài 10: Tạo ma trận 10x10 từ 0.01 đến 1
def bai_10():
    a = np.arange(
        0.01,
        1.01,
        0.01
    ).reshape(10, 10)

    print("\n========== BÀI 10 ==========")
    print(a)

# Bài 11: Tạo array gồm 20 điểm cách đều từ 0 đến 1
def bai_11():
    a = np.linspace(0, 1, 20)

    print("\n========== BÀI 11 ==========")
    print(a)

# NUMPY INDEXING AND SELECTION
# Ma trận dùng chung cho các bài Indexing
def tao_ma_tran():

    mat = np.arange(
        1,
        26
    ).reshape(5, 5)

    return mat

''' Bài 12:
 Lấy ma trận:
    [[12 13 14 15]
    [17 18 19 20]
    [22 23 24 25]]
    '''
def bai_12():

    mat = tao_ma_tran()

    ket_qua = mat[
        2:,
        1:
    ]

    print("\n========== BÀI 12 ==========")
    print(ket_qua)

# Bài 13:
# Lấy giá trị 20
def bai_13():

    mat = tao_ma_tran()

    ket_qua = mat[
        3,
        4
    ]

    print("\n========== BÀI 13 ==========")
    print(ket_qua)


''' Bài 14:
 Lấy ma trận:
    [[ 2]
    [ 7]
    [12]]
'''
def bai_14():

    mat = tao_ma_tran()

    ket_qua = mat[
        :3,
        1:2
    ]

    print("\n========== BÀI 14 ==========")
    print(ket_qua)

'''Bài 15:
  Lấy dòng cuối cùng

  [21 22 23 24 25]'''
def bai_15():

    mat = tao_ma_tran()

    ket_qua = mat[
        4,
        :
    ]

    print("\n========== BÀI 15 ==========")
    print(ket_qua)

'''# Bài 16:
 Lấy 2 dòng cuối

    [[16 17 18 19 20]
    [21 22 23 24 25]]'''
def bai_16():

    mat = tao_ma_tran()

    ket_qua = mat[
        3:,
        :
    ]

    print("\n========== BÀI 16 ==========")
    print(ket_qua)

# Bài 17: Tính tổng tất cả phần tử trong ma trận
def bai_17():

    mat = tao_ma_tran()

    ket_qua = mat.sum()

    print("\n========== BÀI 17 ==========")
    print(ket_qua)

# Bài 18: Tính độ lệch chuẩn của ma trận
def bai_18():

    mat = tao_ma_tran()

    ket_qua = mat.std()

    print("\n========== BÀI 18 ==========")
    print(ket_qua)

# Bài 19: Tính tổng của tất cả các cột
def bai_19():

    mat = tao_ma_tran()

    ket_qua = mat.sum(
        axis=0
    )

    print("\n========== BÀI 19 ==========")
    print(ket_qua)





