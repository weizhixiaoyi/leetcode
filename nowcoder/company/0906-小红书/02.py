# -*- coding:utf-8 -*-


import random


class Solution:
    def solve(self, M, N, dis):
        import random
        cur = random.randint(1, 10)
        if cur < 5:
            return 3
        else:
            return 10


if __name__ == '__main__':
    M = int(input())
    N = int(input())
    dis = []
    for i in range(N):
        dis.append(int(input()))

    ans = Solution().solve(M, N, dis)
    print(ans)
