# coding=utf-8
import clothes
import scipy.special as scsp
import itertools


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


def idol_order(pr, fa, an):
    order = 1
    pr_list = list(itertools.combinations(clothes.Princess, pr))
    fa_list = list(itertools.combinations(clothes.Fairy, fa))
    an_list = list(itertools.combinations(clothes.Angel, an))

    order *= list_product_sum(pr_list) * list_product_sum(fa_list) * list_product_sum(an_list) * scsp.perm(13, 13, True)
    return order


def idol_order_sub(pr, fa, an):
    order = 1
    order *= scsp.comb(17, pr, True)*scsp.comb(17, fa, True)*scsp.comb(18, an, True)*scsp.perm(13, 13, True)
    return order


def idol_all_pattern_sub(pr, fa, an):
    cmr = 1  # 今後実装
    ord = idol_order_sub(pr, fa, an)
    print("Pr:{0}, Fa:{1}, An:{2}, {3:21d}, {4:20d}, {5:20d}".format(pr, fa, an, cmr, ord, cmr * ord))
    return cmr * ord


def idol_all_pattern(pr, fa, an):
    cmr = 1  # 今後実装
    ord = idol_order(pr, fa, an)
    print("Pr:{0:2d}, Fa:{1:2d}, An:{2:2d}, {3:41d}, {4:40d}, {5:40d}".format(pr, fa, an, cmr, ord, cmr * ord))
    return cmr * ord


if __name__ == '__main__':
    print("Pr: , Fa: , An: ,カメラワークのパターン,     アイドルの並べ方,     組み合わせの総数")
    all_pattern = 0
    for i in range(0, 14):
        for j in range(0, 14 - i):
            all_pattern += idol_all_pattern(i, j, 13 - i - j)
    print("")
    print("{:,}通り".format(all_pattern))
