


def cau_2a_thong_ke_luong_theo_nganh(dataset):
    print("\n========== 2a. THỐNG KÊ LƯƠNG THEO NGÀNH ==========")

    ket_qua = dataset.groupby(
        "NganhNghe"
    )["Luong"].agg(
        ["mean", "median", "std"]
    )

    print(ket_qua)

    return ket_qua

def cau_2b_thong_ke_luong_theo_kinh_nghiem(dataset):
    print(
        "\n========== 2b. THỐNG KÊ LƯƠNG THEO KINH NGHIỆM =========="
    )

    ket_qua = dataset.groupby(
        "SoNamKinhNghiem"
    )["Luong"].agg(
        ["mean", "median", "std"]
    )

    print(ket_qua)

    return ket_qua

def cau_2c_luong_binh_quan_theo_nganh(dataset):
    print(
        "\n========== 2c. LƯƠNG BÌNH QUÂN THEO NGÀNH =========="
    )

    ket_qua = dataset.groupby(
        "NganhNghe"
    )["Luong"].mean()

    print(ket_qua)

    return ket_qua
















