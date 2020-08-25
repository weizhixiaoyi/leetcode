# -*- coding:utf-8 -*-


def solve(n):
    if n < 4: return 0
    if n == 4: return 1

    ans = 0
    while n > 3:
        cur_max = 0
        cur_need = 0
        for i in range(10001, 0, -1):
            for j in range(10001, 0, -1):
                need = 2 * i * j + i + j
                if need <= n and i * j > cur_max:
                    cur_max = i * j
                    cur_need = need
        n -= cur_need
        ans += cur_max
    return ans


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        ans = solve(n)
        print(ans)
