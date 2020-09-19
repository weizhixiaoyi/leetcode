# -*- coding:utf-8 -*-
from typing import List


class UnionFind:
    def __init__(self, n):
        self.fa = [i for i in range(n + 1)]

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


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        edges_len = len(edges)
        in_degrees = dict((u + 1, 0) for u in range(edges_len))
        for i in range(edges_len):
            in_degrees[edges[i][1]] += 1

        def judgeCicle(edges, edges_len, removeIdx):
            unionFind = UnionFind(edges_len)
            for i in range(edges_len):
                if i == removeIdx:
                    continue
                if unionFind.union(*edges[i]):
                    return True
            return False

        # 入度为2, 去除节点后无环
        for i in range(edges_len - 1, -1, -1):
            if in_degrees[edges[i][1]] == 2 and judgeCicle(edges, edges_len, i) is False:
                return edges[i]

        # 入度为1, 去除节点后无环
        for i in range(edges_len - 1, -1, -1):
            if judgeCicle(edges, edges_len, i) is False:
                return edges[i]


if __name__ == '__main__':
    # nums = [[1, 2], [1, 3], [2, 3]]
    # nums = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]
    nums = [[2, 1], [3, 1], [4, 2], [1, 4]]
    ans = Solution().findRedundantDirectedConnection(nums)
    print(ans)
