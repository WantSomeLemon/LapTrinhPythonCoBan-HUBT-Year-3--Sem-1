import matplotlib.pyplot as plt
import seaborn as sns

def cau_3a_histplot_luong(dataset):
    print("\n========== 3a. HISTPLOT MỨC LƯƠNG ==========")

    plt.figure(figsize=(8, 5))

    sns.histplot(
        data=dataset,
        x="Luong",
        bins=20,
        kde=True
    )

    plt.title("Phân bố mức lương")
    plt.xlabel("Mức lương")
    plt.ylabel("Số lượng")

    plt.show()


def cau_3b_boxplot_luong_theo_nganh(dataset):
    print("\n========== 3b. BOXPLOT LƯƠNG THEO NGÀNH ==========")

    plt.figure(figsize=(8, 5))

    sns.boxplot(
        data=dataset,
        x="NganhNghe",
        y="Luong"
    )

    plt.title("Mức lương theo ngành")
    plt.xlabel("Ngành nghề")
    plt.ylabel("Mức lương")

    plt.show()

def cau_3c_scatter_kinh_nghiem_luong(dataset):
    print(
        "\n========== 3c. SCATTER KINH NGHIỆM - LƯƠNG =========="
    )

    plt.figure(figsize=(8, 5))

    sns.scatterplot(
        data=dataset,
        x="SoNamKinhNghiem",
        y="Luong"
    )

    plt.title(
        "Mối quan hệ giữa số năm kinh nghiệm và mức lương"
    )

    plt.xlabel("Số năm kinh nghiệm")
    plt.ylabel("Mức lương")

    plt.show()


def cau_3d_bar_luong_trung_binh_theo_nganh(dataset):
    print(
        "\n========== 3d. BAR LƯƠNG TRUNG BÌNH THEO NGÀNH =========="
    )

    luong_trung_binh = dataset.groupby(
        "NganhNghe"
    )["Luong"].mean()

    plt.figure(figsize=(8, 5))

    luong_trung_binh.plot(
        kind="bar"
    )

    plt.title("Lương trung bình theo ngành nghề")
    plt.xlabel("Ngành nghề")
    plt.ylabel("Lương trung bình")

    plt.xticks(rotation=0)

    plt.show()

def cau_3e_bar_luong_binh_quan(dataset):
    print(
        "\n========== 3e. SO SÁNH LƯƠNG BÌNH QUÂN THEO NGÀNH =========="
    )

    luong_binh_quan = dataset.groupby(
        "NganhNghe"
    )["Luong"].mean()

    plt.figure(figsize=(8, 5))

    sns.barplot(
        x=luong_binh_quan.index,
        y=luong_binh_quan.values
    )

    plt.title(
        "So sánh lương bình quân theo ngành nghề"
    )

    plt.xlabel("Ngành nghề")
    plt.ylabel("Lương bình quân")

    plt.show()





