# -*- coding:utf-8 -*-

from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = [v[0] for v in intervals]
        starts_dict = {s: idx for idx, s in enumerate(starts)}
        starts_sort = sorted(starts)
        starts_len = len(starts)
        # print(starts_dict)

        # 寻找第一个大于target的数字, 没有则返回-1
        def binary_search(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    left = mid + 1
                if nums[mid] > target:
                    right = mid - 1
            if (left == starts_len):
                return -1
            return left

        ans = []
        for v in intervals:
            # print(starts_sort)
            # print(v[1])
            idx = binary_search(starts_sort, v[1])
            # print(idx)
            if idx == -1:
                ans.append(-1)
            else:
                ans.append(starts_dict[starts_sort[idx]])
            # print('#' * 10)

        # print(ans)
        return ans


if __name__ == '__main__':
    intervals = [[4, 5], [2, 3], [1, 2]]
    ans = Solution().findRightInterval(intervals)
    print('ans: ', ans)
