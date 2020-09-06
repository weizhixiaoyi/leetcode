# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]):
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if i > j:
                    tmp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = tmp

        # print(matrix)

        for i in range(m):
            line = matrix[i]
            matrix[i] = line[::-1]
        # print(matrix)


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    ans = Solution().rotate(matrix)
    print(ans)
