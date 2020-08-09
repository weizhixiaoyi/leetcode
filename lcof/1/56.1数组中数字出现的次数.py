# -*- coding:utf-8 -*-
from typing import List


class Solution:
    # def singleNumbers(self, nums: List[int]) -> List[int]:
    #     from collections import defaultdict
    #     nums_dict = defaultdict(int)
    #     for num in nums:
    #         nums_dict[num] += 1
    #     ans = []
    #     for key, value in nums_dict.items():
    #         if value == 1:
    #             ans.append(key)
    #     return ans

    def singleNumbers(self, nums: List[int]) -> List[int]:
        import functools
        ret = functools.reduce(lambda x, y: x ^ y, nums)
        # print(ret, bin(ret))

        k = 1
        while ret & k == 0:
            k <<= 1
        # print(k, bin(k))

        a, b = 0, 0
        for num in nums:
            if num & k == 0:
                a ^= num
            else:
                b ^= num
        return [a, b]


if __name__ == '__main__':
    nums = [1, 2, 5, 2]
    ans = Solution().singleNumbers(nums)
    print(ans)
