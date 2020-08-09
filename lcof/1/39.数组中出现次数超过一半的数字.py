# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_len = len(nums)
        target = nums_len // 2
        if nums_len == 1 or nums_len == 2: return nums[0]

        from collections import defaultdict
        nums_dict = defaultdict(int)

        for num in nums:
            nums_dict[num] += 1
            if nums_dict[num] > target:
                return num


if __name__ == '__main__':
    nums = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    ans = Solution().majorityElement(nums)
    print(ans)
