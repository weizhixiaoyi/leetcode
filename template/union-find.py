# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        class unionFind():
            def __init__(self, n):
                self.fa = [i for i in range(n)]
                self.num = n

            # 路径压缩
            def find(self, x):
                if self.fa[x] != x:
                    self.fa[x] = self.find(self.fa[x])
                return self.fa[x]

            def union(self, x, y):
                fx, fy = self.find(x), self.find(y)
                if fx != fy:
                    self.fa[fx] = fy
                    self.num -= 1

        nums = M
        if not nums: return 0
        n = len(nums)

        uf = unionFind(n)
        for i in range(n):
            for j in range(n):
                if nums[i][j] == 1: uf.union(i, j)
        return uf.num


if __name__ == '__main__':
    # M = [[1, 1, 0],
    #      [1, 1, 0],
    #      [0, 0, 1]]
    M = [[1, 1, 0],
         [1, 1, 1],
         [0, 1, 1]]
    ans = Solution().findCircleNum(M)
    print(ans)
