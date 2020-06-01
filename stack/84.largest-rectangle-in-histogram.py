# -*- coding:utf-8 -*-

from typing import List

"""
基本思路是针对每个高度，向周围进行寻找，找到小于当前高度的值，然后便能够得到当前矩阵面积，复杂度O(n**2)。
通过单调栈方法，维持整个数组的单调递增栈。
"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        hlen = len(heights)
        if hlen == 0: return 0
        heights.insert(0, 0)
        heights.append(0)

        st = []
        max_ans = 0
        for i in range(0, len(heights)):
            while (len(st) != 0 and heights[i] < heights[st[-1]]):
                cur_index = st[-1]
                st.pop()
                left = st[-1] + 1
                right = i - 1
                max_ans = max(max_ans, (right - left + 1) * heights[cur_index])

            st.append(i)
        return max_ans


if __name__ == '__main__':
    heights = [2, 1, 5, 6, 2, 3]
    solution = Solution()
    ans = solution.largestRectangleArea(heights)
    print(ans)
