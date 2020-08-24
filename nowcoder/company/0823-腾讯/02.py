# -*- coding:utf-8 -*-


def solve(a, b, c, d):
    if c > d:
        c, d = d, c
    first = (a / 3) * (d ** 3) + (1 / 2) * (d ** 2) + (b * d)
    second = (a / 3) * (c ** 3) + (1 / 2) * (c ** 2) + (b * c)
    ans = first - second
    ans = format(ans, '.6f')
    return ans


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a, b, c, d = map(int, input().split())
        ans = solve(a, b, c, d)
        print(ans)
