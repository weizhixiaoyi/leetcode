# -*- coding:utf-8 -*-


class Solution:
    def solve(self, nums1, nums2, nums3):
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        nums3_len = len(nums3)

        nums = []
        i, j, k = 0, 0, 0
        while i < nums1_len or j < nums2_len or k < nums3_len:
            cur1 = nums1[i] if i < nums1_len else float('inf')
            cur2 = nums2[j] if j < nums2_len else float('inf')
            cur3 = nums3[k] if k < nums3_len else float('inf')
            if cur1 <= cur2 and cur1 <= cur3:
                nums.append(cur1)
                i += 1
                continue
            if cur2 <= cur1 and cur2 <= cur3:
                nums.append(cur2)
                j += 1
                continue
            if cur3 <= cur1 and cur3 <= cur2:
                nums.append(cur3)
                k += 1
                continue
        return nums


if __name__ == '__main__':
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    nums3 = [4, 7, 9]
    ans = Solution().solve(nums1, nums2, nums3)
    print(ans)
