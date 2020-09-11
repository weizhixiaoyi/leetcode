# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] <= nums2[j]:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
            else:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
        while i < 0 and j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1

        while j < 0 and i >= 0:
            nums1[k] = nums1[i]
            k -= 1
            i -= 1

        # print(nums1)


if __name__ == '__main__':
    # nums1, m = [1, 2, 3, 0, 0, 0], 3
    # nums2, n = [4, 5, 6], 3
    nums1, m = [0], 0
    nums2, n = [1], 1
    Solution().merge(nums1, m, nums2, n)
