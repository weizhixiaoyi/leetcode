# -*- coding:utf-8 -*-


def solve(nums):
    if not nums: return 0
    m, n = len(nums), len(nums[0])
    dp = [[0 for j in range(n)] for i in range(m)]
    for i in range(0, m):
        for j in range(0, n):
            if i == 0:
                dp[i][j] = nums[i][j]
                continue
            if j == 0:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j + 1]) + nums[i][j]
                continue
            if j == n - 1:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + nums[i][j]
                continue
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1]) + nums[i][j]
    # print(dp)

    ans = 0
    for j in range(0, n):
        ans = max(ans, dp[m - 1][j])
    return ans


if __name__ == '__main__':
    n = int(input())
    nums, idx = [], 0
    for i in range(n):
        zero_count = (2 * n - 1) // 2 - idx
        line = [0] * zero_count + list(map(int, input().split())) + [0] * zero_count
        nums.append(line)
        idx += 1
    ans = solve(nums)
    print(ans)
