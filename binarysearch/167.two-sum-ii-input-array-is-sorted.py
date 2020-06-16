# -*- coding:utf-8 -*-

from typing import List


class Solution:
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     nums_len = len(numbers)
    #
    #     def binary_search(line, k):
    #         left, right = 0, len(line) - 1
    #         while left <= right:
    #             mid = left + (right - left) // 2
    #             if line[mid] <= k:
    #                 left = mid + 1
    #             if line[mid] > k:
    #                 right = mid - 1
    #         return left - 1 if line[left - 1] == k else -1
    #
    #     for k in range(0, nums_len):
    #         idx = binary_search(numbers, target - numbers[k])
    #         if idx != -1:
    #             return [k + 1, idx + 1]

    # 双指针
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        cur_sum = 0
        left, right = 0, len(numbers) - 1
        while left < right:
            cur_sum = numbers[left] + numbers[right]
            if cur_sum == target:
                return [left + 1, right + 1]
            if cur_sum < target:
                left += 1
            if cur_sum > target:
                right -= 1


if __name__ == '__main__':
    values = [1, 2, 3, 4, 4, 5]
    target = 8
    ans = Solution().twoSum(values, target)
    print('ans: ', ans)
