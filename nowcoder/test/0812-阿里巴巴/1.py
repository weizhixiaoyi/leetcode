# -*- coding:utf-8 -*-

def solve(nums, d):
    if not nums: return 0
    m, n = len(nums), len(nums[0])

    max_value, min_value = 0, float('inf')
    for i in range(m):
        for j in range(n):
            max_value = max(nums[i][j], max_value)

    ans = 0
    for i in range(m):
        for j in range(n):
            ans += (max_value - nums[i][j]) // d
    return ans


if __name__ == '__main__':
    nums = [
        [1, 2, 3],
        [2, 3, 4],
        [2, 3, 1]
    ]
    d = 1
    ans = solve(nums, d)
    print(ans)
