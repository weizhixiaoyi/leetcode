# -*- coding:utf-8 -*-

class Solution:
    def sumNums(self, n: int) -> int:
        import sys
        sys.setrecursionlimit(20000)

        self.res = 0

        def helper(n):
            n > 1 and helper(n - 1)
            self.res += n

        helper(n)
        return self.res


if __name__ == '__main__':
    n = 10000
    ans = Solution().sumNums(n)
    print(ans)
