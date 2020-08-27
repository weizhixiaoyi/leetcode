# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        class unionFind:
            def __init__(self, n):
                self.fa = [i + 1 for i in range(n)]

            # 不能进行路径压缩
            def find(self, x):
                # if x != self.fa[x]:
                #     self.fa[x] = self.find(self.fa[x])
                # return self.fa[x]
                while x != self.fa[x]:
                    x = self.fa[x]
                return x

            def union(self, x, y):
                fx, fy = self.find(x), self.find(y)
                if fx != fy:
                    self.fa[fx] = fy

            def connect(self, x, y):
                fx, fy = self.find(x), self.find(y)
                if fx == fy:
                    return True
                else:
                    return False

        equations_len = len(equations)
        unionfind = unionFind(equations_len)
        equations_set = set()
        for l1, l2 in equations:
            if l1 not in equations_set:
                equations_set.add(l1)
            if l2 not in equations_set:
                equations_set.add(l2)
            unionfind.union(l2, l1)

        ans = []
        for query in queries:
            l1, l2 = query
            if l1 == l2:
                ans.append(1)
            if l1 not in equations_set or l2 not in equations_set:
                ans.append(-1)
            if unionfind.connect(l1, l2):
                ans.append(None)
            else:
                ans.append(-1)


if __name__ == '__main__':
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queryies = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    ans = Solution().calcEquation(equations, values, queryies)
    print(ans)
