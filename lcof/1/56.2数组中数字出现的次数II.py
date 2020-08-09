# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            bit = 1 << i  # 记录当前所才做的bit位
            cnt = 0  # 记录当前为bit有多少1

            for num in nums:
                if num & bit != 0:
                    cnt += 1

            if cnt % 3 != 0:
                ans |= bit
        return ans


if __name__ == '__main__':
    nums = [3, 4, 3, 3]
    # nums = [9, 1, 7, 9, 7, 9, 7]
    ans = Solution().singleNumber(nums)
    print(ans)
