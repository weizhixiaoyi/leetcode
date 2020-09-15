# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key
        nums = list(map(str, nums))

        def cmp(a, b):
            ab, ba = a + b, b + a
            if ab < ba:
                return 1
            elif ab == ba:
                return 0
            else:
                return -1

        nums = sorted(nums, key=cmp_to_key(cmp))
        if nums[0] == '0':
            return '0'
        else:
            return ''.join(nums)


if __name__ == '__main__':
    nums = [3, 30, 34, 5, 9]
    ans = Solution().largestNumber(nums)
    print(ans)
