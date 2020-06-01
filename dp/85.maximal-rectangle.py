# -*- coding:utf-8 -*-

from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp1 = [[0 for j in range(n)] for i in range(m)]
        dp2 = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    dp1[i][j] = 0
                    dp2[i][j] = 0
                    continue
                if i == 0 and j == 0:
                    dp1[i][j] = int(matrix[i][j])
                    dp2[i][j] = int(matrix[i][j])
                    continue
                if i == 0:
                    dp1[i][j] = dp1[i][j - 1] + 1
                    continue
                if j == 0:
                    dp2[i][j] = dp2[i - 1][j] + 1
                    continue

                dp1[i][j] = min(dp1[i - 1][j], dp1[i - 1][j - 1]) + 1
                dp2[i][j] = min(dp2[i][j - 1], dp2[i - 1][j - 1]) + 1
        print(dp1)
        print(dp2)
        mul = [[dp1[i][j] * dp2[i][j] for j in range(n)] for i in range(m)]
        max_value = max(map(max, mul))
        return max_value


if __name__ == '__main__':
    matrix1 = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    matrix = [["0", "1"], ["0", "1"]]
    solution = Solution()
    ans = solution.maximalRectangle(matrix1)
    print('ans: ', ans)
