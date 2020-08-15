# -*- coding:utf-8 -*-

def quickMul(x, n):
    if x == 0: return 0

    res = 1
    if n < 0: x, n = 1 / x, -n
    while n:
        if n & 1: res = res * x
        x = x * x
        n = n >> 1
    return res


if __name__ == '__main__':
    x, n = 2, 5
    print(quickMul(x, n))
