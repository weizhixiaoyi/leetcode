# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        s = {0}
        ans, cur_sum = 0, 0
        for num in nums:
            cur_sum += num

            if cur_sum - target in s:
                cur_sum = 0
                ans += 1
                s = {0}
            else:
                s.add(cur_sum)
        return ans


if __name__ == '__main__':
    # nums = [-1, 3, 5, 1, 4, 2, -9]
    # target = 6
    nums = [2, 5, 3, 5, 9, 4, 3, 5]
    target = 9
    ans = Solution().maxNonOverlapping(nums, target)
    print(ans)
