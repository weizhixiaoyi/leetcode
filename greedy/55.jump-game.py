# -*- coding:utf-8 -*-
from typing import List


class Solution:
    # 维护能够达到的最远位置
    # 如果当前位置在最远位置之内, 那么一定是能够到达当前点的, 那么则进行更新最远位置
    def canJump(self, nums: List[int]) -> bool:
        nums_len = len(nums)
        rightmost = 0
        for i in range(0, nums_len):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if i >= nums_len - 1:
                    return True
        return False



if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    ans = Solution().canJump(nums)
    print(ans)
