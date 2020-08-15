# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums: return 0

        nums_len = len(nums)
        left, right = 0, nums_len - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            if nums[mid] > target:
                right = mid - 1
        return left
