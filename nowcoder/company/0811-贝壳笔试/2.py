# -*- coding:utf-8 -*-

def solve(a, b):
    if a <= b:
        return 'inf'
    else:
        ans = 0
        for x in range(1, 10000000):
            if a % x == b:
                # print(a, x, b)
                ans += 1

        return ans


if __name__ == '__main__':
    # ab = list(map(int, input().split()))
    # a, b = ab[0], ab[1]
    a, b = 10000, 56
    ans = solve(a, b)
    print(ans)
