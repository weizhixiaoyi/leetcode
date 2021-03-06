# -*- coding:utf-8 -*-

from functools import reduce


def get_C(n, k):
    import math
    if n == k: return 1
    if k == 1: return n
    mul_n = math.factorial(n)
    mul_k = math.factorial(k)
    mul_n_k = math.factorial(n - k)
    return mul_n // (mul_k * mul_n_k)


def solve(n):
    ans = 0
    value = 1000000007

    if n % 2 == 0:
        for i in range(1, n // 2 + 1):
            a = get_C(n, i)
            b = get_C(i, 1)
            print(a * b, end=' ')
            ans += (a * b % value)
        ans = (ans * 2) % value
        return ans
    else:
        for i in range(1, n // 2 + 1):
            a = get_C(n, i)
            b = i
            print(a, b, a * b)
            ans += (a * b % value)
        ans = (ans * 2) % value
        ans = ans + (get_C(n, n // 2 + 1) * get_C(n // 2 + 1, 1)) % value
        return ans


if __name__ == '__main__':
    # n = int(input())
    n = 5
    # ans = solve(n)
    # print(ans)
