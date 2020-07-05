# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        nums_len = len(nums)
        if nums_len == 0: return 0
        if nums_len == 1: return 1
        if nums_len == 2 and nums[0] != nums[1]: return 2

        up, down = 1, 1
        for i in range(1, nums_len):
            if nums[i] > nums[i - 1]:
                up = down + 1
            if nums[i] < nums[i - 1]:
                down = up + 1
        return max(up, down)



if __name__ == '__main__':
    # nums = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
    # nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    nums = [0, 1]
    ans = Solution().wiggleMaxLength(nums)
    print('ans: ', ans)
