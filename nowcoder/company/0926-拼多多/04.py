# -*- coding:utf-8 -*-


class Solution:
    def solve(self, n, m):
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        for i in range(0, m + 1):
            dp[i][0] = 1

        for j in range(0, n + 1):
            dp[0][j] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i < 2 or j < 2:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                else:
                    dp[i][j] = (max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + dp[i - 2][j - 2])
        print(dp)


if __name__ == '__main__':
    # n, m = map(int, input().split())
    # n, m = 4, 2
    n, m = 2, 5
    ans = Solution().solve(n, m)
    print(ans)
