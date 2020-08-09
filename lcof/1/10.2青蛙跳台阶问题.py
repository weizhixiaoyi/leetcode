# -*- coding:utf-8 -*-

class Solution:
    def numWays(self, n: int) -> int:
        self.ans = [0 for i in range(101)]

        def helper(n):
            if n == 0 or n == 1:
                self.ans[n] = 1

            if self.ans[n] != 0:
                return self.ans[n]
            self.ans[n] = helper(n - 1) + helper(n - 2)
            return self.ans[n]

        helper(n)
        return self.ans[n] % 1000000007


if __name__ == '__main__':
    n = 1
    ans = Solution().numWays(n)
    print(ans)
