# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1: return []

        nums1_len, nums2_len = len(nums1), len(nums2)
        from collections import defaultdict
        ans_dict = defaultdict(int)

        stack = []
        for i in range(nums2_len):
            while stack and nums2[stack[-1]] < nums2[i]:
                cur = stack.pop()
                ans_dict[nums2[cur]] = nums2[i]

            stack.append(i)
        for i in range(len(stack)):
            ans_dict[nums2[stack[i]]] = -1
        stack.clear()

        ans = []
        for i in range(nums1_len):
            ans.append(ans_dict[nums1[i]])
        return ans


if __name__ == '__main__':
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    ans = Solution().nextGreaterElement(nums1, nums2)
    print(ans)
