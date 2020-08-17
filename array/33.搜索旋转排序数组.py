# -*- coding:utf-8 -*-
from typing import List


class Solution:
    """
    # 递归搜索其实还是遍历了整个数组, 复杂度O(n)
    def search(self, nums: List[int], target: int) -> int:
        nums_len = len(nums)
        if nums_len == 1 and nums[0] == target: return 0
        if nums_len == 1 and nums[0] != target: return -1
        self.ans = -1

        def dfs(l, r, nums):
            if nums[l] == target:
                self.ans = l
            if l >= r: return
            # print(l, r, nums[l], nums[r])

            mid = (l + r) // 2
            dfs(l, mid, nums)
            dfs(mid + 1, r, nums)

        dfs(0, nums_len - 1, nums)
        return self.ans
    """

    def binary_search(self, nums, target):
        pass

    def search(self, nums: List[int], target: int) -> int:
        nums_len = len(nums)
        left, right = 0, nums_len - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            if nums[mid] < nums[right]:
                right = mid

        ans1 = self.binary_search(nums, target)
        ans2 = self.binary_search(nums, target)


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    # nums = [1]
    # target = 1
    # nums = [1, 3]
    # target = 3
    ans = Solution().search(nums, target)
    print(ans)
