# -*- coding:utf-8 -*-


def solve(nums, nums_len):
    dp1 = [1 for i in range(nums_len)]
    for i in range(nums_len):
        for j in range(0, i):
            if nums[j] > nums[i]:
                dp1[i] = max(dp1[i], dp1[j] + 1)
            else:
                dp1[i] = dp1[j]
    # print(dp1)
    dp2 = [1 for i in range(nums_len)]
    nums_rev = nums[::-1]
    for i in range(nums_len):
        for j in range(0, i):
            if nums_rev[j] > nums_rev[i]:
                dp2[i] = max(dp2[i], dp2[j] + 1)
            else:
                dp2[i] = dp2[j]
    # print(dp2)
    ans = 0
    for i in range(nums_len - 1):
        for j in range(i + 1, nums_len):
            if nums[i] == nums[j]:
                print(nums[i], dp1[i], dp2[nums_len - j - 1])
                ans = max(ans, 2 * min(dp1[i], dp2[nums_len - j - 1]))
    # print()
    return ans


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        ans = solve(nums, n)
        print(ans)
