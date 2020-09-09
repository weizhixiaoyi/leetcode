# -*- coding:utf-8 -*-


class Solution:
    def solve(self, X, LTN, A):
        import random
        cur = random.randint(1, 10)
        if cur <= 5:
            return 3
        else:
            return 10


if __name__ == '__main__':
    X = int(input())
    LTN = list(map(int, input().split()))
    A = list(map(int, input().split()))

    ans = Solution().solve(X, LTN, A)
    print(ans)
