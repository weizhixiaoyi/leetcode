# -*- coding:utf-8 -*-
from typing import List


class Solution:
    """
    def trap(self, height: List[int]) -> int:
        ans = 0
        height_len = len(height)
        for k in range(1, height_len - 1):
            left, right = k, k
            max_left, max_right = 0, 0
            while left >= 0:
                max_left = max(max_left, height[left])
                left -= 1
            while right < height_len:
                max_right = max(max_right, height[right])
                right += 1
            ans += min(max_left, max_right) - height[k]
        return ans
    """

    def trap(self, height: List[int]) -> int:
        height_len = len(height)

        ans = 0
        stack = []
        for i in range(height_len):
            while stack and height[stack[-1]] < height[i]:
                cur = stack.pop()
                if not stack: break

                left, right = stack[-1], i
                ans += (right - left - 1) * (min(height[right], height[left]) - height[cur])
            stack.append(i)
        return ans


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    # height = [0]
    # height = [2, 6, 3, 8, 2, 7, 2, 5, 0]
    ans = Solution().trap(height)
    print(ans)
