# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums_len = len(nums)
        repeat = 0
        for i in range(0, nums_len):
            while i != nums[i]:
                print(i, nums)
                if nums[i] == nums[nums[i]]:
                    repeat = nums[i]
                    break
                temp = nums[i]
                nums[i] = nums[temp]
                nums[temp] = temp
        return repeat


if __name__ == '__main__':
    nums = [2, 3, 1, 0, 2, 5, 3]
    ans = Solution().findRepeatNumber(nums)
    print(ans)
