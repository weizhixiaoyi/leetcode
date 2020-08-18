# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums: return False
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            # print(left, mid, right)
            if nums[mid] == target:
                return True
            if nums[left] == nums[mid]:
                left += 1
                continue
            # if nums[right] == nums[mid]:
            #     right -= 1
            #     continue
            if nums[mid] <= nums[right]:
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return False


if __name__ == '__main__':
    # nums = [2, 5, 6, 0, 0, 1, 2]
    # target = 2
    # nums = [1, 2, 1]
    # target = 2
    nums = [3, 1, 1, 1]
    target = 1
    ans = Solution().search(nums, target)
    print(ans)

"""
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums: return False
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right + 1) // 2
            # print(left, mid, right)
            if nums[left] == nums[mid]:
                left += 1
                continue
            if nums[right] == nums[mid]:
                right -= 1
                continue
            if nums[mid] < nums[right]:
                # 在有序数组中查找
                if nums[mid] <= target and target <= nums[right]:
                    left = mid
                else:
                    right = mid - 1
            else:
                if nums[left] <= target and target <= nums[mid - 1]:
                    right = mid - 1
                else:
                    left = mid
        # print(left)
        if nums[left] == target:
            return True
        else:
            return False
"""
