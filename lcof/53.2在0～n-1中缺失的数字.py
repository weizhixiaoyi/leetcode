# -*- coding:utf-8 -*-
from typing import List


class Solution:
    # def missingNumber(self, nums: List[int]) -> int:
    #     nums_len = len(nums)
    #
    #     def helper(left, right):
    #         if right - left + 1 <= 2:
    #             if left != nums[left] and self.flag is False:
    #                 self.ans = left
    #                 self.flag = True
    #             if right != nums[right] and self.flag is False:
    #                 self.ans = right
    #                 self.flag = True
    #             return None
    #
    #         mid = (left + right) // 2
    #         helper(left, mid)
    #         helper(mid + 1, right)
    #
    #     self.ans = -1
    #     self.flag = False
    #     helper(0, nums_len - 1)
    #     if self.ans == -1:
    #         return nums_len
    #     else:
    #         return self.ans

    def missingNumber(self, nums: List[int]) -> int:
        nums_len = len(nums)

        left, right = 0, nums_len - 1
        while left <= right:
            mid = (left + right) // 2
            # print(mid, nums[mid])
            if nums[mid] == mid:
                left = mid + 1
            if nums[mid] > mid:
                right = mid - 1

        return left


if __name__ == '__main__':
    nums = [0, 1, 2, 3, 4, 5]
    ans = Solution().missingNumber(nums)
    print(ans)
