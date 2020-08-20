# -*- coding:utf-8 -*-


class Solution:
    def waysToStep(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        if n == 3: return 4
        dp = [0 for i in range(n)]
        dp[0], dp[1], dp[2] = 1, 2, 4
        for i in range(3, n):
            dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000007
        # print(dp)
        return dp[n - 1]


if __name__ == '__main__':
    n = 5
    ans = Solution().waysToStep(n)
    print(ans)
