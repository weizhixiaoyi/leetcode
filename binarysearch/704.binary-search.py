# -*- coding:utf-8 -*-

from typing import List


# 对于没有找到的元素, 返回low则表示应该要插入的位置
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:  # 搜索区间为空
            mid = left + (right - left) // 2  # 可以防止数过大导致溢出
            # print(mid, left, right)
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return -1
        # return low


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    target = 0
    ans = Solution().search(nums, target)
    print('ans: ', ans)
