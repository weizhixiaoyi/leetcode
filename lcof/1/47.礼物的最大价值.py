# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

        for i in range(0, m):
            for j in range(0, n):
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j]) + grid[i][j]

        return dp[m][n]


if __name__ == '__main__':
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    ans = Solution().maxValue(grid)
    print(ans)
