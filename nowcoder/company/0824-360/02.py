# -*- coding:utf-8 -*-


def solve(n, nums):
    nums = sorted(nums, key=lambda d: (d[1]))
    nums_len = len(nums)
    ans = 0
    for a, b in nums:
        ans += a
    return ans


if __name__ == '__main__':
    n = int(input())
    nums = []
    for i in range(n):
        a, b = map(int, input().split())
        nums.append([a, b])
    ans = solve(n, nums)
    print(ans)
