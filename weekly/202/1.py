# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        arr_len = len(arr)
        if arr_len <= 2: return False
        for i in range(0, arr_len - 2):
            f1, f2, f3 = arr[i] % 2, arr[i + 1] % 2, arr[i + 2] % 2
            if f1 and f2 and f3:
                return True
        return False


if __name__ == '__main__':
    # arr = [1, 2, 34, 3, 4, 5, 7, 23, 12]
    arr = [2, 6, 4, 1]
    ans = Solution().threeConsecutiveOdds(arr)
    print(ans)
