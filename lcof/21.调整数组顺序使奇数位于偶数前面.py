# -*- coding:utf-8 -*-

from typing import List


class Solution:
    # def exchange(self, nums: List[int]) -> List[int]:
    #     nums_len = len(nums)
    #     if nums_len == 0: return []
    #     if nums_len == 1: return nums
    #
    #     nums1, nums2 = [], []
    #     for i in range(nums_len):
    #         if nums[i] % 2 != 0:
    #             nums1.append(nums[i])
    #         else:
    #             nums2.append(nums[i])
    #
    #     return nums1 + nums2

    def exchange(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        if nums_len == 0: return []
        if nums_len == 1: return nums

        i, j = 0, nums_len - 1
        while i < j:
            if nums[i] % 2 != 0:
                i += 1

            if nums[j] % 2 == 0:
                j -= 1

            if i < j:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp

        # print(nums)
        return nums


if __name__ == '__main__':
    # nums = [1, 2, 3, 4]
    nums = [2, 16, 3, 5, 13, 1, 16, 1, 12, 18, 11, 8, 11, 11, 5, 1]
    ans = Solution().exchange(nums)
    print(ans)
