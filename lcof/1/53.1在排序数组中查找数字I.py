# -*- coding:utf-8 -*-
from typing import List


class Solution:
    # O(n)
    # def search(self, nums: List[int], target: int) -> int:
    #     if not nums: return 0
    #
    #     from collections import defaultdict
    #     nums_dict = defaultdict(int)
    #     for num in nums:
    #         nums_dict[num] += 1
    #     return nums_dict[target]

    def search(self, nums: List[int], target: int) -> int:
        if not nums: return 0

        nums_len = len(nums)

        def helper1(target):
            left, right = 0, nums_len - 1
            if nums[-1] < target:
                return -1

            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                if nums[mid] >= target:
                    right = mid - 1

            return left if nums[left] == target else -1

        def helper2(target):
            left, right = 0, nums_len - 1

            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    left = mid + 1
                if nums[mid] > target:
                    right = mid - 1

            return left - 1 if nums[left - 1] == target else -1

        idx1 = helper1(target)
        if idx1 != -1:
            return helper2(target) - idx1 + 1
        else:
            return 0


if __name__ == '__main__':
    # nums = [5, 7, 7, 8, 8, 10]
    # target = 6
    nums = [4, 4]
    target = 3
    ans = Solution().search(nums, target)
    print(ans)
