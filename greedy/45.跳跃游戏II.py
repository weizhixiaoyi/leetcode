# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        nums_len = len(nums)
        if not nums or nums_len == 1: return 0

        end = 0
        ans = 0
        right_value = nums[0]
        for i in range(nums_len - 1):
            right_value = max(right_value, i + nums[i])
            if i == end:
                end = right_value
                ans += 1

        return ans


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    # nums = [1, 2]
    ans = Solution().jump(nums)
    print(ans)
