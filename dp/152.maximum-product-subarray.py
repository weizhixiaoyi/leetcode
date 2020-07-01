# -*- coding:utf-8 -*-

from typing import List


class Solution:
    # 以0进行分割, 然后以无0子数组进行判断dp[j]/dp[i-1]寻找最大值, 复杂度O(n*n)
    """
    def maxProduct(self, nums: List[int]) -> int:
        nums_len = len(nums)
        if nums_len == 0: return None
        if nums_len == 1: return nums[0]

        zero_flag = False
        if 0 in nums: zero_flag = True
        values, value = [], [1]
        for i in range(nums_len):
            if nums[i] == 0:
                values.append(value)
                value = [1]
                continue
            value.append(nums[i])
        if value: values.append(value)

        max_value = []
        for value in values:
            # print(value)
            multi = [value[0]]
            value_len = len(value)
            for i in range(1, value_len):
                multi.append(multi[i - 1] * value[i])
            # print(multi)

            cur_max_value = -10000
            for i in range(0, value_len - 1):
                for j in range(i + 1, value_len):
                    cur_max_value = max(cur_max_value, multi[j] // multi[i])
            max_value.append(cur_max_value)
        # print(max_value)
        max_ans = max(max_value)
        if max_ans < 0 and zero_flag: return 0
        if max_ans < 0 and zero_flag is False: return max_ans
        return max_ans
    """

    # 复杂度O(n)
    def maxProduct(self, nums: List[int]) -> int:
        nums_len = len(nums)
        if nums_len == 0: return None
        if nums_len == 1: return nums[0]

        dp_min = 1
        dp_max = 1
        max_value = -1000000
        for i in range(nums_len):
            if nums[i] < 0:
                # 如果是符号, 最大值变为最小值, 最小值变为最大值
                dp_min, dp_max = dp_max, dp_min

            # 进行位置截断和判断最大值
            dp_max = max(dp_max * nums[i], nums[i])
            dp_min = min(dp_min * nums[i], nums[i])
            max_value = max(max_value, dp_max)
        # print(max_value)
        return max_value


if __name__ == '__main__':
    nums = [2, 3, -2, 4]
    ans = Solution().maxProduct(nums)
    print(ans)
