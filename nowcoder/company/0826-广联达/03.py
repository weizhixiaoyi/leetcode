# -*- coding:utf-8 -*-


def solve(nums_len, nums):
    nums = [val - 1 for val in nums]
    nums_sort = sorted(nums)
    # print(nums)
    # print(nums_sort)

    ans = 0
    for i in range(nums_len):
        while i != nums[i]:
            ans += 1
            tmp = nums[i]
            nums[i] = nums[tmp]
            nums[tmp] = tmp
    print(nums)
    return ans


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    ans = solve(n, nums)
    print(ans)
