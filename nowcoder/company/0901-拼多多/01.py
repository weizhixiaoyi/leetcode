# -*- coding:utf-8 -*-

import pprint


def solve(n):
    nums = [[0 for j in range(n)] for i in range(n)]
    m, n = n, n
    if n % 2 == 1:
        half_m, half_n = (m + 1) // 2, (n + 1) // 2

        # 1, 8
        for i in range(0, half_m - 1):
            for j in range(half_n, n):
                if i == j: continue
                if i == n - j - 1: continue
                if i < n - j - 1:
                    nums[i][j] = 1
                else:
                    nums[i][j] = 8

        # 2, 3
        for i in range(0, half_m - 1):
            for j in range(0, half_n - 1):
                if i == j: continue
                if i == n - j - 1: continue
                if i < j:
                    nums[i][j] = 2
                else:
                    nums[i][j] = 3

        # 4, 5
        for i in range(half_m, m):
            for j in range(0, half_n - 1):
                if i == j: continue
                if i == n - j - 1: continue
                if i < n - j - 1:
                    nums[i][j] = 4
                else:
                    nums[i][j] = 5

        # 6, 7
        for i in range(half_m, m):
            for j in range(half_n, n):
                if i == j: continue
                if i == n - j - 1: continue
                if i < j:
                    nums[i][j] = 7
                else:
                    nums[i][j] = 6
    else:
        half_m, half_n = m // 2, n // 2

        # 1, 8
        for i in range(0, half_m):
            for j in range(half_n, n):
                if i == j: continue
                if i == n - j - 1: continue
                if i < n - j - 1:
                    nums[i][j] = 1
                else:
                    nums[i][j] = 8

        # 2, 3
        for i in range(0, half_m):
            for j in range(0, half_n):
                if i == j: continue
                if i == n - j - 1: continue
                if i < j:
                    nums[i][j] = 2
                else:
                    nums[i][j] = 3

        # 4, 5
        for i in range(half_m, m):
            for j in range(0, half_n):
                if i == j: continue
                if i == n - j - 1: continue
                if i < n - j - 1:
                    nums[i][j] = 4
                else:
                    nums[i][j] = 5

        # 6, 7
        for i in range(half_m, m):
            for j in range(half_n, n):
                if i == j: continue
                if i == n - j - 1: continue
                if i < j:
                    nums[i][j] = 7
                else:
                    nums[i][j] = 6

    # pprint.pprint(nums, width=20)
    for val in nums:
        val = [str(v) for v in val]
        print(' '.join(val))


if __name__ == '__main__':
    n = int(input())
    # n = 4
    # n = 7
    # n = 5
    solve(n)
