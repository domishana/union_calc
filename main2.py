# coding=utf-8
import scipy.special as scsp
import itertools
import clothes


def list_product(int_list):
    product = 1
    for elm in int_list:
        product *= elm
    return product


def list_product_sum(int_list_list):
    sum_number = 0
    for el_list in int_list_list:
        sum_number += list_product(el_list)
    return sum_number


def idol_camera(pr, fa, an):
    pattern = 2

    if pr == 0:
        pattern *= 5 * 4 * 4 * 4 * 5
    elif pr == 1:
        pass
    elif pr == 2:
        pattern *= 2
    else:
        pattern *= pr ** 2 * (pr - 1) ** 3

    if an == 0:
        pattern *= 5 * 4 * 4 * 4 * 5
    elif an == 1:
        pass
    elif an == 2:
        pattern *= 2
    else:
        pattern *= an ** 2 * (an - 1) ** 3

    if fa == 0:
        pattern *= 5 * 4 * 5
    elif fa == 1:
        pass
    elif fa == 2:
        pattern *= 2 * 2
    else:
        pattern *= fa ** 2 * (fa - 1)

    return pattern


def idol_order(pr, fa, an):
    order = 1
    pr_list = list(itertools.combinations(clothes.Princess, pr))
    fa_list = list(itertools.combinations(clothes.Fairy, fa))
    an_list = list(itertools.combinations(clothes.Angel, an))

    order *= list_product_sum(pr_list) * list_product_sum(fa_list) * list_product_sum(an_list) * scsp.perm(5, 5, True)
    return order


def idol_order_sub(pr, fa, an):
    order = 1
    order *= scsp.comb(17, pr, True)*scsp.comb(17, fa, True)*scsp.comb(18, an, True)*scsp.perm(5, 5, True)
    return order


def idol_all_pattern(pr, fa, an):
    cmr = idol_camera(pr, fa, an)
    ord = idol_order(pr, fa, an)
    print("Pr:{0}, Fa:{1}, An:{2}, {3:21d}, {4:20d}, {5:20d}".format(pr, fa, an, cmr, ord, cmr * ord))
    return cmr * ord


def idol_all_pattern_sub(pr, fa, an):
    cmr = idol_camera(pr, fa, an)
    ord = idol_order_sub(pr, fa, an)
    print("Pr:{0}, Fa:{1}, An:{2}, {3:21d}, {4:20d}, {5:20d}".format(pr, fa, an, cmr, ord, cmr * ord))
    return cmr * ord


if __name__ == '__main__':
    print("Pr: , Fa: , An: ,カメラワークのパターン,     アイドルの並べ方,     組み合わせの総数")
    all_pattern = 0
    for i in range(0, 6):
        for j in range(0, 6 - i):
            all_pattern += idol_all_pattern(i, j, 5 - i - j)
            all_pattern += idol_all_pattern_sub(i, j, 5-i-j)
    print("")
    print("{:,}通り".format(all_pattern))
