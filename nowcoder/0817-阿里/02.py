# -*- coding:utf-8 -*-


def solve(n, h):
    mod = 1e9 + 7
    dp = [[0 for j in range(n + 1)] for i in range(n + 1)]
    # dp[i][j]代表i个结点不超过j的方案数
    for i in range(1, n + 1):
        dp[0][i - 1] = 1
        for j in range(1, n + 1):
            for k in range(j):
                dp[j][i] = (dp[j][i] % mod + dp[k][i - 1] * dp[j - k - 1][i - 1] % mod) % mod
    # print(dp[n][h])
    return dp[n][h]


if __name__ == '__main__':
    n, h = 3, 2
    ans = solve(n, h)
    print(ans)
