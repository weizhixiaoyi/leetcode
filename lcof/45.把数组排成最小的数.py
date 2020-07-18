# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        nums_len = len(nums)
        if nums_len == 0: return ''
        if nums_len == 1: return str(nums[0])

        def helper(nums):
            # 返回值是根据当前数组得到的最小排列
            if len(nums) == 1:
                return [nums[0]]

            min_path = helper(nums[:-1])

            # 头部插入
            cur_min_value = nums[-1] + ''.join(min_path)
            cur_min_path = [nums[-1]] + min_path
            # 插入中间
            for k in range(1, len(min_path)):
                temp_min_value = ''.join(min_path[:k]) + nums[-1] + ''.join(min_path[k:])
                if temp_min_value < cur_min_value:
                    cur_min_value = temp_min_value
                    cur_min_path = min_path[:k] + [nums[-1]] + min_path[k:]
            # 插入末尾
            if ''.join(min_path) + nums[-1] < cur_min_value:
                cur_min_path = min_path + [nums[-1]]

            return cur_min_path

        nums = [str(num) for num in nums]
        ans = helper(nums)
        return ''.join(ans)


if __name__ == '__main__':
    # nums = [3, 30, 34, 5, 9]
    nums = [10, 2]
    ans = Solution().minNumber(nums)
    print(ans)
