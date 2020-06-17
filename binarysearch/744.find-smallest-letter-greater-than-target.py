# -*- coding:utf-8 -*-

from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1]:
            return letters[0]

        left, right = 0, len(letters) - 1
        while left <= right:
            mid = left + (right - left) // 2
            # if letters[mid] == target:
            #     return letters[mid + 1]
            if letters[mid] <= target:
                left = mid + 1
            if letters[mid] > target:
                right = mid - 1
        # return letters[left]
        return letters[left]


if __name__ == '__main__':
    letters = ["c", "f", "j"]
    target = "d"
    ans = Solution().nextGreatestLetter(letters, target)
    print('ans: ', ans)
