# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        if not mat: return 0
        m, n = len(mat), len(mat[0])

        ans = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and self.isValid(i, j, mat, m, n):
                    ans += 1
        return ans

    def isValid(self, i, j, mat, m, n):
        for k in range(n):
            if k == j: continue
            if mat[i][k] == 1: return False
        for k in range(m):
            if k == i: continue
            if mat[k][j] == 1: return False
        return True


if __name__ == '__main__':
    mat = [[1, 0, 0],
           [0, 1, 0],
           [0, 0, 1]]
    ans = Solution().numSpecial(mat)
    print(ans)
