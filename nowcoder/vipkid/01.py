# -*- coding:utf-8 -*-


def solve(nums):
    if not nums: return 0
    nums_len = len(nums)
    dp = [1 for i in range(nums_len)]
    for i in range(nums_len):
        for j in range(i + 1):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
            else:
                dp[i] = dp[j]
    # print(dp)
    return dp[nums_len - 1]


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    # nums = [10, 9, 2, 5, 3, 7, 101, 18]
    ans = solve(nums)
    print(ans)
