# -*- coding:utf-8 -*-
from typing import List


class Solution:
    # 递归
    # def canPartition(self, nums: List[int]) -> bool:
    #     nums_sum = sum(nums)
    #     if nums_sum % 2 != 0: return False
    #
    #     target = nums_sum // 2
    #     if nums[-1] == target:
    #         return True
    #     if nums[-1] > target:
    #         return False
    #
    #     def helper(target, index):
    #         if target == 0:
    #             return True
    #         if target < 0 or index < 0:
    #             return False
    #
    #         if helper(target - nums[index], index - 1):
    #             return True
    #         if helper(target, index - 1):
    #             return True
    #         return False
    #
    #     ans = helper(target, len(nums) - 1)
    #     return ans

    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        nums_len = len(nums)
        if nums_sum % 2 != 0: return False

        nums = sorted(nums)
        target = nums_sum // 2
        if nums[-1] == target:
            return True
        if nums[-1] > target:
            return False

        dp = [float('-inf') for i in range(target + 1)]
        dp[0] = 0
        for i in range(nums_len):
            for j in range(target, nums[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - nums[i]] + 1)

        if dp[-1] == float('-inf'):
            return False
        else:
            return True

if __name__ == '__main__':
    # nums = [1, 5, 11, 5]
    # nums = [1, 2, 3, 4]
    # nums = [1, 2, 3, 5]
    nums = [2, 2, 3, 5]
    ans = Solution().canPartition(nums)
    print(ans)
