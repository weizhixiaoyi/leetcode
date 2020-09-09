# -*- coding:utf-8 -*-


class Solution:
    def solve(self, X, LTN, A):
        return 1


if __name__ == '__main__':
    X = int(input())
    LTN = list(map(int, input().split()))
    A = list(map(int, input().split()))

    ans = Solution().solve(X, LTN, A)
    print(ans)
