# -*- coding:utf-8 -*-

class Solution:
    def solve(self, n):
        dp = [0 for i in range(n + 1)]
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        # print(dp)
        return dp[n]


if __name__ == '__main__':
    n = 10
    ans = Solution().solve(n)
    print(ans)
