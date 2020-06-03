# -*- coding:utf-8 -*-

from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0: return False
        target = sum(nums) // k

        import functools
        @functools.lru_cache(None)
        def search(nums, k, target, cur, start, used):
            # 递归截止条件
            if k == 1: return True

            # 相等则构建下一个集合
            if cur == target:
                return search(nums, k - 1, target, 0, 0, used)

            for i in range(start, len(nums)):
                if (not used[i]) and (cur + nums[i] <= target):
                    used[i] = True
                    if search(nums, k, target, cur + nums[i], i, used): return True
                    used[i] = False

            return False

        nums.sort()
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1

        used = [False] * len(nums)
        return search(nums, k, target, 0, 0, used)


if __name__ == '__main__':
    nums, k = [1, 1, 1, 1, 1], 1
    solution = Solution()
    ans = solution.canPartitionKSubsets(nums, k)
    print(ans)
