# -*- coding:utf-8 -*-

# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def nSum(self, n, nums, start, target):
        ans = []
        nums_len = len(nums)
        if n < 2 or nums_len < 2: return [[]]

        if n == 2:
            left, right = start, nums_len - 1
            while left < right:
                left_num, right_num = nums[left], nums[right]
                cur_sum = left_num + right_num
                if cur_sum == target:
                    ans.append([left_num, right_num])
                    while left < right and nums[left] == left_num: left += 1
                    while left < right and nums[right] == right_num: right -= 1
                if cur_sum < target:
                    while left < right and nums[left] == left_num: left += 1
                if cur_sum > target:
                    while left < right and nums[right] == right_num: right -= 1
        else:
            for i in range(start, nums_len):
                sub = self.nSum(n - 1, nums, i + 1, target - nums[i])
                for arr in sub:
                    ans.append([nums[i]] + arr)
                # 此处保证新增加的元素不会重复
                while i < nums_len - 1 and nums[i] == nums[i + 1]: i += 1

        return ans


if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    nums.sort()
    n = 4
    target = 0
    ans = Solution().nSum(n, nums, 0, target)
    print(ans)
