# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums_len = len(nums)

        ans = []

        from copy import deepcopy
        def helper(start, path):
            ans.append(deepcopy(path))

            for k in range(start, nums_len):
                path.append(nums[k])
                helper(k + 1, path)
                path.pop()

        helper(0, [])
        return ans


if __name__ == '__main__':
    nums = [1, 2, 3]
    ans = Solution().subsets(nums)
    print(ans)
