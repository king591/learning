# -*- coding: utf-8 -*
# 从文本list_later.txt读取一个数列，并将数列按从大到小排序后存到list_done.txt


def check_list(a):
    if type(a) != list:
        print('这不是一个合法的列表')
    else:
        i = 0
        n = len(a) - 1
        while i in range(0, n):
            if type(a[i]) != int and type(a[i]) != float:
                # 列表既不是整形也不是浮点
                # print('列表元素不是纯数值，无法计算')
                return False
            else:
                i += 1
    return True


def list_ing(a):
    s = 0
    n = len(a) - 1
    while s in range(0, n):
        i = 0
        while i in range(0, n):
            if a[i] > a[i + 1]:
                temp = a[i]
                a[i] = a[i + 1]
                a[i + 1] = temp
                i += 1
            else:
                i += 1
        s += 1
    return a


a_list = [1, 54, 6541, 651, 84, 651, 65, 16, 1446, 51, 3241, 6541, 6, 1651]
print(a_list)
check_list(a_list)
a_list_ed = list_ing(a_list)
print(a_list_ed)
