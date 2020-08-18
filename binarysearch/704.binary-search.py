# -*- coding:utf-8 -*-

from typing import List


# 对于没有找到的元素, 返回low则表示应该要插入的位置
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right + 1) // 2
            # 先写能够排出的逻辑, 比较好想
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid

        return left if nums[left] == target else -1


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    target = 5
    ans = Solution().search(nums, target)
    print(ans)
