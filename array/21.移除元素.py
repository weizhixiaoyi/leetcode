# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: return 0

        nums_len = len(nums)
        l, r = 0, 0
        while r < nums_len:
            if nums[r] == val:
                r += 1
                continue
            else:
                nums[l] = nums[r]
                l += 1
                r += 1
        return l


if __name__ == '__main__':
    # nums = [0, 1, 2, 2, 3, 0, 4, 2]
    # val = 2
    nums = [3, 2, 2, 3]
    val = 2
    ans = Solution().removeElement(nums, val)
    print(nums, ans)
