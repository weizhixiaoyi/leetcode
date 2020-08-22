# -*- coding:utf-8 -*-


def could(n, m, k):
    need = 0
    for i in range(n):
        need += k
        if k % 2 == 0:
            k = k // 2
        else:
            k = k // 2 + 1
    if need > m:
        return False
    return True


def solve(n, m):
    left, right = 1, m
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        # print(mid, could(n, m, mid))
        if could(n, m, mid):
            ans = max(ans, mid)
            left = mid + 1
        else:
            right = mid - 1
    # return left
    return ans


if __name__ == '__main__':
    n, m = map(int, input().split())
    # n, m = 3, 7
    # n, m = 58, 80
    ans = solve(n, m)
    print(ans)
