# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]

        def binary_search1(nums, target):
            left, right = 0, len(nums) - 1
            while left < right:
                mid = (left + right) // 2
                # 不满足的条件
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left if nums[left] == target else -1

        def binary_search2(nums, target):
            left, right = 0, len(nums) - 1
            while left < right:
                mid = (left + right + 1) // 2
                # print(left, mid, right)
                # 不满足的条件
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid
            return left if nums[left] == target else -1

        ans1 = binary_search1(nums, target)
        if ans1 == -1: return [-1, -1]
        ans2 = binary_search2(nums, target)
        return [ans1, ans2]


if __name__ == '__main__':
    # nums = [5, 7, 7, 8, 8, 10]
    # target = 8
    nums = [3, 3, 3, 3, 3, 3, 4, 5]
    target = 3
    ans = Solution().searchRange(nums, target)
    print(ans)
