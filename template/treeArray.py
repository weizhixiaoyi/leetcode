# -*- coding:utf-8 -*-


class treeArray:
    def __init__(self, n):
        self.n = n
        self.c = [0 for i in range(n)]

    def lowbit(self, x):
        return x & (-x)

    def update(self, i, k):
        while i < self.n:
            self.c[i] += k
            i += self.lowbit(i)

    def query(self, i):
        res = 0
        while i > 0:
            res += self.c[i]
            i -= self.lowbit(i)
        return res
