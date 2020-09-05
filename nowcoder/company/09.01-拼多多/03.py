# -*- coding:utf-8 -*-


def solve(n, m, weight, value):
    dp = [0 for i in range(m + 1)]

    for i in range(n):
        for j in range(m, weight[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

    # print(dp[m])
    return dp[m]


if __name__ == '__main__':
    n, m = map(int, input().split())
    weight, value = [], []
    for i in range(n):
        a, b = map(int, input().split())
        weight.append(a)
        value.append(b)

    ans = solve(n, m, weight, value)
    print(ans)
