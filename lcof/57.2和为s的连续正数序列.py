# -*- coding:utf-8 -*-
from typing import List


class Solution:
    # O(nlogn)
    # def findContinuousSequence(self, target: int) -> List[List[int]]:
    #     max_value = (target + 1) // 2
    #     nums = [i + 1 for i in range(max_value)]
    #     nums_len = max_value
    #
    #     def helper(cur_target):
    #         left, right = 0, nums_len - 1
    #
    #         while left <= right:
    #             mid = (left + right) // 2
    #             cur_value = nums[mid] * (nums[mid] + 1)
    #             if cur_value == cur_target:
    #                 return nums[mid]
    #             if cur_value < cur_target:
    #                 left = mid + 1
    #             if cur_value > cur_target:
    #                 right = mid - 1
    #
    #         return -1
    #
    #     ans = []
    #     for i in range(nums_len):
    #         cur_target = 2 * target + nums[i] * (nums[i] - 1)
    #         flag = helper(cur_target)
    #         if flag != -1:
    #             ans.append(nums[i: flag])
    #     return ans

    def findContinuousSequence(self, target: int) -> List[List[int]]:
        max_value = (target + 1) // 2
        nums = [i + 1 for i in range(max_value)]
        nums_len = len(nums)

        from copy import deepcopy
        start, cur_sum = 0, 0
        ans, cur_nums = [], []
        for end in range(0, nums_len):
            cur_sum += nums[end]
            cur_nums.append(nums[end])

            while cur_sum > target:
                cur_sum -= nums[start]
                start += 1
                cur_nums = cur_nums[1:]

            if cur_sum == target:
                ans.append(deepcopy(cur_nums))

                cur_sum -= nums[start]
                start += 1
                cur_nums = cur_nums[1:]

        return ans


if __name__ == '__main__':
    target = 50252
    ans = Solution().findContinuousSequence(target)
    print(ans)
