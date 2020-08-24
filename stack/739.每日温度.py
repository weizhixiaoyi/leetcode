# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not T: return []

        nums = T
        nums_len = len(nums)
        ans, stack = [0 for i in range(nums_len)], []
        for i in range(0, nums_len):
            while stack and nums[stack[-1]] < nums[i]:
                cur = stack.pop()

                ans[cur] = i - cur

            stack.append(i)
        return ans


if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    ans = Solution().dailyTemperatures(temperatures)
    print(ans)
