# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        if not matrix: return ans
        m, n = len(matrix), len(matrix[0])
        l, r, t, b = 0, n - 1, 0, m - 1

        while matrix:
            # left to right
            for k in range(l, r + 1): ans.append(matrix[t][k])
            t += 1
            if t > b: break

            # top to bottom
            for k in range(t, b + 1): ans.append(matrix[k][r])
            r -= 1
            if l > r: break

            # right to left
            for k in range(r, l - 1, -1): ans.append(matrix[b][k])
            b -= 1
            if t > b: break

            # tail to head
            for k in range(b, t - 1, -1): ans.append(matrix[k][l])
            l += 1
            if l > r: break

        return ans


if __name__ == '__main__':
    # matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ans = Solution().spiralOrder(matrix)
    print(ans)
