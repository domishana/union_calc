# coding=utf-8

# test
import scipy.special as scsp


def idol_camera(pr, fa, an):
    pattern = 2

    if pr == 0:
        pattern *= 5*4*4*4*5
    elif pr == 1:
        pass
    elif pr == 2:
        pattern *= 2
    else:
        pattern *= pr**2 * (pr-1)**3

    if an == 0:
        pattern *= 5*4*4*4*5
    elif an == 1:
        pass
    elif an == 2:
        pattern *= 2
    else:
        pattern *= an**2 * (an-1)**3

    if fa == 0:
        pattern *= 5*4*5
    elif fa == 1:
        pass
    elif fa == 2:
        pattern *= 2*2
    else:
        pattern *= fa**2 * (fa-1)

    return pattern


def idol_order(pr, fa, an):
    order = 1
    order *= scsp.comb(17, pr, True)*scsp.comb(17, fa, True)*scsp.comb(18, an, True)*scsp.perm(5, 5, True)
    return order


def idol_all_pattern(pr, fa, an):
    cmr = idol_camera(pr, fa, an)
    ord = idol_order(pr, fa, an)
    print("Pr:{0}, Fa:{1}, An:{2}, {3:20d}, {4:20d}, {5:20d}".format(pr, fa, an, cmr, ord, cmr*ord))
    return cmr*ord


Princess = [13, 14, 14, 12, 10, 10, 11, 12, 12, 10, 14, 12, 10, 11, 12, 11, 13]
Fairy = [10, 10, 12, 13, 10, 12, 11, 10, 10, 10, 12, 12, 13, 14, 14, 12, 11]
Angel = [14, 11, 11, 11, 14, 11, 13, 12, 10, 11, 13, 11, 12, 12, 12, 12, 10, 11]

if __name__ == '__main__':
    all_pattern = 0
    for i in range(0, 6):
        for j in range(0, 6-i):
            all_pattern += idol_all_pattern(i, j, 5-i-j)
    print(all_pattern)
