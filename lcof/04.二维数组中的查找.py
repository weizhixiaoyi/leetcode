# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0: return False
        n = len(matrix[0])
        if n == 0: return False

        def binary_search(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return True

                if nums[mid] < target:
                    left = mid + 1
                if nums[mid] > target:
                    right = mid - 1

            return False

        for line in matrix:
            ans = binary_search(line, target)
            if ans is True:
                return True
        return False



if __name__ == '__main__':
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    # target = 5
    target = 20
    ans = Solution().findNumberIn2DArray(matrix, target)
    print(ans)
