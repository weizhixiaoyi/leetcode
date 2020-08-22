# -*- coding:utf-8 -*-

def solve(n, m):
    return (n * m) // 2


if __name__ == '__main__':
    # n, m = 8, 2
    n, m = map(int, input().split())
    ans = solve(n, m)
    print(ans)
