# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        class unionFind:
            def __init__(self, n):
                self.fa = [i for i in range(n + 1)]

            # 路径压缩查找
            def find(self, x):
                if self.fa[x] != x:
                    self.fa[x] = self.find(self.fa[x])
                return self.fa[x]

            def union(self, x, y):
                fx, fy = self.find(x), self.find(y)
                if fx == fy:
                    return True
                else:
                    self.fa[fx] = fy
                    return False

        edges_len = len(edges)
        unionfind = unionFind(edges_len)
        for edge in edges:
            x, y = edge
            if unionfind.union(x, y):
                return [x, y]


if __name__ == '__main__':
    # edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    edges = [[1, 2], [1, 3], [2, 3]]
    ans = Solution().findRedundantConnection(edges)
    print(ans)
