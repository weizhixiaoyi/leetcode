# -*- coding:utf-8 -*-
from typing import List


class Solution:
    """
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if not graph: return False
        node_len = len(graph)
        node = [0 for i in range(node_len)]

        from queue import Queue
        q = Queue()
        for i in range(node_len):
            if node[i] != 0: continue

            node[i] = 1
            q.put(i)
            while not q.empty():
                node_idx = q.get()

                for v in graph[node_idx]:
                    if node[v] == node[node_idx]:
                        return False
                    if node[v] == 0:
                        node[v] = -node[node_idx]
                        q.put(v)
        return True
    """

    def isBipartite(self, graph: List[List[int]]) -> bool:
        if not graph: return False

        class UnionFind:
            def __init__(self, n):
                self.fa = [i for i in range(n)]

            def find(self, x):
                if self.fa[x] != x:
                    self.fa[x] = self.find(self.fa[x])
                return self.fa[x]

            def union(self, x, y):
                fx, fy = self.find(x), self.find(y)
                if fx != fy:
                    self.fa[fx] = fy

            def iscon(self, x, y):
                return self.fa[x] == self.fa[y]

        graph_len = len(graph)
        unionfind = UnionFind(graph_len)
        for i in range(graph_len):
            for v in graph[i]:
                if unionfind.iscon(i, v):
                    return False
                unionfind.union(graph[i][0], v)
        return True


if __name__ == '__main__':
    # graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
    graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
    # graph = [[4], [], [4], [4], [0, 2, 3]]
    # graph = [[2, 4], [2, 3, 4], [0, 1], [1], [0, 1], [7], [9], [5], [], [6], [12, 14], [], [10], [], [10], [19], [18],
    #          [], [16], [15], [23], [23], [], [20, 21], [], [], [27], [26], [], [], [34], [33, 34], [], [31], [30, 31],
    #          [38, 39], [37, 38, 39], [36], [35, 36], [35, 36], [43], [], [], [40], [], [49], [47, 48, 49], [46, 48, 49],
    #          [46, 47, 49], [45, 46, 47, 48]]
    ans = Solution().isBipartite(graph)
    print(ans)
