# -*- coding:utf-8 -*-

from typing import List
import pprint


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        for i in range(0, m):
            for j in range(0, n):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                    continue
                if i == 0 or j == 0:
                    dp[i][j] = 1
                    continue

                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        max_value = max(map(max, dp))
        return max_value ** 2


if __name__ == '__main__':
    # matrix = [
    #     [1, 0, 1, 0, 0],
    #     [1, 0, 1, 1, 1],
    #     [1, 1, 1, 1, 1],
    #     [1, 0, 0, 1, 0]
    # ]
    matrix = [["0", "0", "0", "1"], ["1", "1", "0", "1"], ["1", "1", "1", "1"], ["0", "1", "1", "1"],
              ["0", "1", "1", "1"]]
    matrix = [[str(v) for v in line] for line in matrix]
    solution = Solution()
    ans = solution.maximalSquare(matrix)
    print('ans: ', ans)
