# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        a_len = len(a)
        if a_len == 1: return [a[0]]

        left, right = [], []
        left_val, right_val = 1, 1
        for i in range(a_len):
            left_val *= a[i]
            left.append(left_val)
            right_val *= a[a_len - i - 1]
            right.append(right_val)
        right.reverse()

        ans = []
        for k in range(0, a_len):
            if k == 0:
                ans.append(right[1])
                continue
            if k == a_len - 1:
                ans.append(left[a_len - 1 - 1])
                continue
            ans.append(left[k - 1] * right[k + 1])
        return ans


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    # nums = [1, 2]
    ans = Solution().constructArr(nums)
    print(ans)
