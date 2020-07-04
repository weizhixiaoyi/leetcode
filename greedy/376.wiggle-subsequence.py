# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        nums_len = len(nums)
        if nums_len == 1: return 1
        if nums_len == 2 and nums[0] != nums[1]: return 2



if __name__ == '__main__':
    nums = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
    # nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ans = Solution().wiggleMaxLength(nums)
    print('ans: ', ans)
