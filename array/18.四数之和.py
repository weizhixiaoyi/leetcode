# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        nums_len = len(nums)
        ans_set = set()
        for i in range(nums_len - 1):
            cur_nums = nums[i + 1:]
            three_sum_ans = self.threeSum(cur_nums, target - nums[i])
            for three in three_sum_ans:
                cur_ans = (nums[i], three[0], three[1], three[2])
                if cur_ans not in ans_set: ans_set.add(cur_ans)
        ans = [list(val) for val in ans_set]
        return ans

    def threeSum(self, nums: List[int], target) -> List[List[int]]:
        nums.sort()
        nums_len = len(nums)

        ans_set = set()
        for index in range(0, nums_len - 2):
            cur_target = target - nums[index]

            i, j = index + 1, nums_len - 1
            while i < j:
                left, right = nums[i], nums[j]
                cur_sum = nums[i] + nums[j]
                if cur_sum == cur_target:
                    cur_ans = (nums[index], nums[i], nums[j])
                    if cur_ans not in ans_set: ans_set.add(cur_ans)
                    while left == nums[i] and i < j: i += 1
                    while right == nums[j] and i < j: j -= 1
                if cur_sum < cur_target:
                    while left == nums[i] and i < j: i += 1
                if cur_sum > cur_target:
                    while right == nums[j] and i < j: j -= 1

        ans = [list(val) for val in ans_set]
        return ans


if __name__ == '__main__':
    nums = [0, 0, 0, 0]
    target = 1
    ans = Solution().fourSum(nums, target)
    print(ans)
