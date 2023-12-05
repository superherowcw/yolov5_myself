import numpy as np
import time


# np.random.seed(666)


def time_wcw():
    return time.time()


def sort_wcw(a):
    try:
        if isinstance(a, str):
            if a > '0' and a < '9':
                return np.sort([int(i) for i in a])
        return np.sort(a)
    except ValueError:
        return '字符串的值应为0-9 ！'


# 换位
def swap(a, b):
    temp = a
    a = b
    b = temp


# 冒泡排序
def sort_wcw_s(a):
    for j in range(len(a)):
        for i in range(len(a)):
            if a[i - 1] > a[i] and i != 0:
                a[i - 1], a[i] = a[i], a[i - 1]

    return a


# 随机数， 时间统计
def a_random(a):
    m = time.time()
    return a[np.random.randint(0, len(a) - 1)], m


# 快速排序
def quick_sort_wcw(a):
    if len(a) <= 1:
        return a
    else:
        a_ones = a[0]
        a_min = [i for i in a[1:] if i <= a_ones]
        a_max = [i for i in a[1:] if i > a_ones]
        return quick_sort_wcw(a_min) + [a_ones] + quick_sort_wcw(a_max)


# 随机抽选
def np_2103():
    name_dict = {
        1: '穆光逾',
        2: '余琪',
        3: '左晓琪',
        4: '吴崇稳',
        5: '秦闻强',
        6: '陆鑫',
        7: '谷浩林',
        8: '吴梦周',
        9: '邓玉书',
        10: '李鹏飞',
        11: '常涛',
        12: '李赫',
        13: '李少博',
        14: '胡利杰',
        15: '夏振钧',
        16: '于泽',
        17: '张博文',
        18: '林俊昊',
    }
    return name_dict[np.random.randint(1, 19)]


print(np_2103())
