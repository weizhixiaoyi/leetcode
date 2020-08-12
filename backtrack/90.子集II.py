# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        nums_len = len(nums)
        used = [False for i in range(nums_len)]

        from copy import deepcopy
        ans = []

        def helper(start, path):
            ans.append(deepcopy(path))

            for k in range(start, nums_len):
                if k > 0 and nums[k] == nums[k - 1] and not used[k - 1]: continue
                path.append(nums[k])
                used[k] = True
                helper(k + 1, path)
                used[k] = False
                path.pop()

        helper(0, [])
        return ans


if __name__ == '__main__':
    # nums = [1, 2, 2]
    nums = [4, 4, 4, 1, 4]
    ans = Solution().subsetsWithDup(nums)
    print(ans)
