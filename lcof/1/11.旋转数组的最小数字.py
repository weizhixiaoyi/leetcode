# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        nums_len = len(numbers)
        if nums_len == 1: return numbers[0]

        min_value = numbers[0]
        for i in range(1, nums_len):
            if numbers[i] < numbers[i - 1]:
                min_value = numbers[i]
                return min_value
        return min_value


if __name__ == '__main__':
    # numbers = [3, 4, 5, 1, 2]
    numbers = [2, 2, 2, 0, 1]
    ans = Solution().minArray(numbers)
    print(ans)
