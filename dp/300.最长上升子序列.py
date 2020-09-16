# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        nums_len = len(nums)
        tails = [0 for i in range(nums_len)]

        res = 0
        for num in nums:
            left, right = 0, res
            while left < right:
                mid = (left + right) // 2
                if tails[mid] >= num:
                    right = mid
                else:
                    left = mid + 1
            tails[left] = num
            if left == res: res += 1
        return res


if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    ans = Solution().lengthOfLIS(nums)
    print(ans)