# -*- coding:utf-8 -*-
from typing import List


class Solution:
    # 常规递归方法
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums_len = len(nums)
        if nums_len == 0: return [[]]
        if nums_len == 1: return [[nums[0]]]

        self.ans = [[nums[0]]]

        def helper(nums):
            if len(nums) == 0: return

            pre_ans, self.ans = self.ans, []
            cur_num = nums[0]
            for cur_nums in pre_ans:
                # 插入头部
                self.ans.append([cur_num] + cur_nums)
                # 插入中间
                for i in range(1, len(cur_nums)):
                    self.ans.append(cur_nums[:i] + [cur_num] + cur_nums[i:])
                # 插入尾部
                self.ans.append(cur_nums + [cur_num])
            helper(nums[1:])

        helper(nums[1:])
        return self.ans
    """

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        from copy import deepcopy
        def helper(nums, track):
            if len(track) == len(nums):
                self.ans.append(deepcopy(track))

            for i in range(len(nums)):
                # 已经走过的路径不在候选集之中
                if nums[i] in track:
                    continue
                track.append(nums[i])
                helper(nums, track)
                track.remove(nums[i])

        helper(nums, [])
        return self.ans


if __name__ == '__main__':
    nums = [i for i in range(1, 3 + 1)]
    ans = Solution().permute(nums)
    print(ans)
