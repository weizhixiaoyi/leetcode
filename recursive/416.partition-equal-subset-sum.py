# -*- coding:utf-8 -*-

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2 != 0: return False

        def helper(cur, index):
            diff = cur - nums[index]
            if diff == 0:
                return True
            if diff < 0:
                return False

            for k in range(index):
                if helper(diff, index - k - 1):
                    return True
            return False

        target = nums_sum // 2
        nums_len = len(nums)
        nums.sort()
        if nums[-1] == target:
            return True
        if nums[-1] > target:
            return False
        ans = helper(target, nums_len - 1)
        return ans


if __name__ == '__main__':
    nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 97, 95]
    ans = Solution().canPartition(nums)
    print(ans)
