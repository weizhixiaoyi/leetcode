# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        self.ans = []
        from copy import deepcopy
        def helper(nums, track, used):
            if len(track) == len(nums):
                self.ans.append(deepcopy(track))

            for i in range(len(nums)):
                if used[i]: continue
                # 如果当前节点和上一个节点相同, 则没必要再次进行访问
                # 如果nums[i] == nums[i-1]相等且not used[i - 1], 则说明上一个节点已经访问过, 不需要再次进行访问
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]: continue

                used[i] = True
                track.append(nums[i])
                helper(nums, track, used)
                used[i] = False
                track.pop()

        nums.sort()
        used = [False for i in range(len(nums))]
        helper(nums, [], used)
        return self.ans


if __name__ == '__main__':
    nums = [2, 2, 1, 1]
    ans = Solution().permuteUnique(nums)
    print(ans)
