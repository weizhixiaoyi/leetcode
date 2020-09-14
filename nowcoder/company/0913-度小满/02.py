# -*- coding:utf-8 -*-


def solve(nums, nums_len):
    value = 1000000007
    dp = [1 for i in range(nums_len)]
    for i in range(nums_len):
        for j in range(0, i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(dp)
    max_len = max(dp)
    if max_len == 1:
        return dp.count(1) % value
    else:
        return dp.count(max_len - 1) % value


if __name__ == '__main__':
    # n = int(input())
    # nums = list(map(int, input().split()))
    n = 5
    nums = [1, 3, 6, 4, 7]
    # n = 4
    # nums = [4, 3, 2, 1]
    ans = solve(nums, n)
    print(ans)
