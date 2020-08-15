# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0

        nums_len = len(nums)
        l, r = 0, 0
        while r < nums_len:
            while r < nums_len and nums[r] == nums[l]:
                r += 1

            if r < nums_len:
                l += 1
                nums[l] = nums[r]
        return l + 1


if __name__ == '__main__':
    # nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    nums = [1, 1, 2]
    ans = Solution().removeDuplicates(nums)
    print(nums, ans)
