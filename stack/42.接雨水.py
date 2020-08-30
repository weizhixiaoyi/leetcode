# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        height_len = len(height)
        ans, stack = 0, []
        for i in range(height_len):
            while stack and height[stack[-1]] < height[i]:
                cur = stack.pop()
                if not stack: break

                left, right = stack[-1], i
                # print(left, right)
                ans += (right - left - 1) * (min(height[left], height[right]) - height[cur])

            stack.append(i)
        return ans


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    # height = [3, 2, 1, 0, 1, 2]
    ans = Solution().trap(height)
    print(ans)
