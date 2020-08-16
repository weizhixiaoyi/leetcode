# -*- coding:utf-8 -*-

class Solution:
    """
    def minDays(self, n: int) -> int:
        dp = [0 for i in range(n + 1)]
        dp[1] = 1
        for i in range(2, n + 1):
            if i % 2 == 0 and i % 3 == 0:
                dp[i] = min(dp[i - 1], dp[i // 2], dp[i // 3]) + 1
                continue
            if i % 2 == 0:
                dp[i] = min(dp[i - 1], dp[i // 2]) + 1
                continue
            if i % 3 == 0:
                dp[i] = min(dp[i - 1], dp[i // 3]) + 1
                continue

            dp[i] = dp[i - 1] + 1
        # print(dp)
        return dp[n]
    """

    def minDays(self, n: int) -> int:
        self.ans = 0

        dict = {}

        def dfs(n):
            if n == 1: return 1
            if n == 2: return 2
            if n in dict: return dict[n]

            cur_value = min(dfs(n // 3) + n % 3, dfs(n // 2) + n % 2) + 1
            dict[n] = cur_value
            return cur_value

        ans = dfs(n)
        return ans


if __name__ == '__main__':
    # n = 56
    n = 182
    ans = Solution().minDays(n)
    print(ans)
