# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1_len, nums2_len = len(nums1), len(nums2)
        left = (nums1_len + nums2_len + 1) // 2
        right = (nums1_len + nums2_len + 2) // 2
        return (self.get_k_min(nums1, 0, nums1_len - 1, nums2, 0, nums2_len - 1, left) +
                self.get_k_min(nums1, 0, nums1_len - 1, nums2, 0, nums2_len - 1, right)) / 2

    def get_k_min(self, nums1, start1, end1, nums2, start2, end2, k):
        len1 = end1 - start1 + 1
        len2 = end2 - start2 + 1
        if len1 > len2: return self.get_k_min(nums2, start2, end2, nums1, start1, end1, k)
        if len1 == 0: return nums2[start2 + k - 1]
        if k == 1: return min(nums1[start1], nums2[start2])

        i = start1 + min(len1, k // 2) - 1
        j = start2 + min(len2, k // 2) - 1
        if nums1[i] > nums2[j]:
            return self.get_k_min(nums1, start1, end1, nums2, j + 1, end2, k - (j - start2 + 1))
        else:
            return self.get_k_min(nums1, i + 1, end1, nums2, start2, end2, k - (i - start1 + 1))

if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2, 4]
    ans = Solution().findMedianSortedArrays(nums1, nums2)
    print(ans)