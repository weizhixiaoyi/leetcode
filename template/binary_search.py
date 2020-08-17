# -*- coding:utf-8 -*-

from typing import List


# 判断target是否存在于nums之中, 没有则返回-1
def binary_search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:  # 搜索区间为空
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        if nums[mid] > target:
            right = mid - 1

    return -1


# 搜索第一个出现的数字, 没有出现则返回-1
def lower_search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        print(left, mid, right)
        if nums[mid] < target:
            left = mid + 1
        if nums[mid] >= target:  # 找到相等的时候，也继续进行查找
            right = mid - 1

    return left if nums[left] == target else -1


# 搜索最后一个出现的数字
def upper_search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        print(left, mid, right)
        if nums[mid] <= target:
            left = mid + 1
        if nums[mid] > target:
            right = mid - 1

    return left - 1 if nums[left - 1] == target else -1


if __name__ == '__main__':
    nums, target = [1, 2, 2, 2, 3, 4, 5], 2

    print('binary_search')
    ans1 = binary_search(nums, target)
    print(ans1, end='\n\n')

    print("low_search")
    ans2 = lower_search(nums, target)
    print(ans2, end='\n\n')

    print('upper_search')
    ans2 = upper_search(nums, target)
    print(ans2)
