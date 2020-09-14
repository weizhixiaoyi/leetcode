# -*- coding:utf-8 -*-

from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_len, nums2_len = len(nums1), len(nums2)
        if nums1_len > nums2_len:
            nums1, nums2 = nums2, nums1
            nums1_len, nums2_len = nums2_len, nums1_len
        nums1, nums2 = sorted(nums1), sorted(nums2)
        # print(nums1, nums2)
        from collections import Counter
        nums1_count = Counter(nums1)

        ans = []
        for num in nums2:
            if num in nums1_count and nums1_count[num] > 0:
                ans.append(num)
                nums1_count[num] -= 1
        return ans


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    # nums1 = [3, 1, 2]
    # nums2 = [1, 1]
    ans = Solution().intersect(nums1, nums2)
    print(ans)
