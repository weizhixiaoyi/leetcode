# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        nums_len = len(nums)

        min_value = float('inf')
        ans = 0
        for k in range(nums_len - 2):
            cur_target = target - nums[k]

            left, right = k + 1, nums_len - 1
            # print(left, right)
            while left < right:
                left_value, right_value = nums[left], nums[right]
                cur_sum = left_value + right_value
                cur_diff = abs(cur_target - cur_sum)

                if cur_sum == cur_target:
                    return target
                if cur_diff < min_value:
                    # print(nums[k], left_value, right_value)
                    min_value = cur_diff
                    ans = cur_sum + nums[k]
                if cur_sum < cur_target:
                    while left < right and nums[left] == left_value: left += 1
                if cur_sum > cur_target:
                    while left < right and nums[right] == right_value: right -= 1

        return ans


if __name__ == '__main__':
    # nums = [-1, 2, 1, -4]
    # target = 1
    nums = [1, 1, 1, 2]
    target = 3
    ans = Solution().threeSumClosest(nums, target)
    print(ans)
