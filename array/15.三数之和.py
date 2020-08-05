# -*- coding:utf-8 -*-

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        nums_len = len(nums)

        ans_set = set()
        for index in range(0, nums_len - 2):
            target = -nums[index]

            i, j = index + 1, nums_len - 1
            while i < j:
                left, right = nums[i], nums[j]
                cur_sum = nums[i] + nums[j]
                if cur_sum == target:
                    cur_ans = (nums[index], nums[i], nums[j])
                    if cur_ans not in ans_set: ans_set.add(cur_ans)
                    while left == nums[i] and i < j: i += 1
                    while right == nums[j] and i < j: j -= 1
                if cur_sum < target:
                    while left == nums[i] and i < j: i += 1
                if cur_sum > target:
                    while right == nums[j] and i < j: j -= 1

        ans = [list(val) for val in ans_set]
        return ans


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    ans = Solution().threeSum(nums)
    print(ans)
