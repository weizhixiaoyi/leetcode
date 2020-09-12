# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums: return 1
        nums_len = len(nums)

        for i in range(nums_len):
            while nums[i] > 0 and nums[i] <= nums_len and nums[i] != i + 1 and nums[nums[i] - 1] != nums[i]:
                # swap
                tmp = nums[i]
                nums[i] = nums[tmp - 1]
                nums[tmp - 1] = tmp
        # print(nums)

        for i in range(nums_len):
            if nums[i] != i + 1:
                return i + 1
        return nums_len + 1


if __name__ == '__main__':
    # nums = [3, 4, -1, 1]
    # nums = [1]
    nums = [0, 1, 2]
    ans = Solution().firstMissingPositive(nums)
    print(ans)
