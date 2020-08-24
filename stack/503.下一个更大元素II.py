# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums: return []

        nums = nums + nums
        nums_len = len(nums)
        stack = []
        tmp = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                cur = stack.pop()
                tmp.append([cur, nums[i]])

            stack.append(i)

        for i in range(len(stack)):
            tmp.append([stack[i], -1])
        tmp = sorted(tmp, key=lambda d: d[0])
        ans = []
        for i in range(nums_len // 2):
            ans.append(tmp[i][1])
        return ans


if __name__ == '__main__':
    # nums = [4, 2, 3, 1]
    nums = [1, 2, 1]
    ans = Solution().nextGreaterElements(nums)
    print(ans)
