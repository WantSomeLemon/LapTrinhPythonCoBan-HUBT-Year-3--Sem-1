import numpy as np
import matplotlib.pyplot as plt



# ============================================================
# PHẦN 2: BÀI TẬP VỀ MATPLOTLIB
# ============================================================

# Dữ liệu dùng cho Matplotlib
def tao_du_lieu_matplotlib():

    x = np.arange(
        0,
        100
    )

    y = x * 2

    z = x ** 2

    return x, y, z

''' Matplotlib - Exercise 1
 Tạo figure và axes bằng add_axes
 tại [0, 0, 1, 1]'''
def matplotlib_bai_1():

    x, y, z = tao_du_lieu_matplotlib()

    fig = plt.figure()

    ax = fig.add_axes(
        [0, 0, 1, 1]
    )

    ax.plot(x,y)

    ax.set_xlabel("X")

    ax.set_ylabel("Y")

    ax.set_title("Plot of X and Y")

    plt.show()

''' Matplotlib - Exercise 2

 Tạo figure có 2 axes:
    ax1: [0, 0, 1, 1]
    ax2: [0.2, 0.5, .2, .2]
 Sau đó plot x,y trên cả hai axes'''
def matplotlib_bai_2():

    x, y, z = tao_du_lieu_matplotlib()

    fig = plt.figure()

    ax1 = fig.add_axes(
        [0, 0, 1, 1]
    )

    ax2 = fig.add_axes(
        [0.2, 0.5, 0.2, 0.2]
    )

    ax1.plot(x,y)

    ax2.plot(x,y)

    plt.show()

''' Matplotlib - Exercise 3

# Tạo 2 axes:
    ax1: [0, 0, 1, 1]
    ax2: [0.2, 0.5, .4, .4]
 Sử dụng x, y, z để tạo biểu đồ'''
def matplotlib_bai_3():

    x, y, z = tao_du_lieu_matplotlib()

    fig = plt.figure()

    ax1 = fig.add_axes(
        [0, 0, 1, 1]
    )

    ax2 = fig.add_axes(
        [0.2, 0.5, 0.4, 0.4]
    )

    ax1.plot(x,z)

    ax2.plot(x,y)

    ax2.set_xlim(
        [20, 22]
    )

    ax2.set_ylim(
        [30, 50]
    )

    plt.show()