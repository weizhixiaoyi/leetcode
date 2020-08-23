# -*- coding:utf-8 -*-
from typing import List


class Solution:
    """
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums: return 0
        if sum(nums) < s: return 0
        nums_len = len(nums)
        pre_sum, pre = 0, [0]
        for i in range(nums_len):
            pre_sum += nums[i]
            pre.append(pre_sum)

        def check(k):
            for i in range(k, len(pre)):
                if pre[i] - pre[i - k] >= s:
                    return True
            return False

        left, right = 0, nums_len - 1
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        # print(left)
        return left
    """

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums: return 0
        if sum(nums) < s: return 0
        nums_len = len(nums)

        ans = nums_len
        start, cur_sum = 0, 0
        for i in range(nums_len):
            # 窗口右移
            cur_sum += nums[i]

            # 达到条件, 窗口左边移动
            while cur_sum >= s:
                cur_sum -= nums[start]
                ans = min(ans, i - start + 1)
                start += 1
        # print(ans)
        return ans


if __name__ == '__main__':
    s = 7
    nums = [2, 3, 1, 2, 4, 3]
    ans = Solution().minSubArrayLen(s, nums)
    print(ans)