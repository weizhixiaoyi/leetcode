# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums_set = set()

        for num in nums:
            if num in nums_set:
                return num
            nums_set.add(num)


if __name__ == '__main__':
    nums = [2, 3, 1, 0, 2, 5, 3]
    ans = Solution().findRepeatNumber(nums)
    print(ans)
