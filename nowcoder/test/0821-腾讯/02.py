# -*- coding:utf-8 -*-

def solve(nums, nums_len):
    nums = sorted(nums, reverse=True)
    nums1, nums2 = [], []
    idx = 0
    for num in nums:
        if idx % 2 == 0:
            nums1.append(num)
        else:
            nums2.append(num)
        idx += 1
    return sum(nums1) - sum(nums2)


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    # n = 3
    # nums = [2, 7, 4]
    # n = 4
    # nums = [1, 2, 3, 4]
    ans = solve(nums, n)
    print(ans)
