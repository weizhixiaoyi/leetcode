# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums_len = len(nums)

        ans = []

        def helper(start, path):
            ans.append(path)

            for k in range(start, nums_len):
                helper(k + 1, path + [nums[k]])

        helper(0, [])
        return ans


if __name__ == '__main__':
    nums = [1, 2, 3]
    ans = Solution().subsets(nums)
    print(ans)
