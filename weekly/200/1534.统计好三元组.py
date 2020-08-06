# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        arr_len = len(arr)
        ans = 0
        for i in range(arr_len - 2):
            for j in range(i + 1, arr_len - 1):
                for k in range(j + 1, arr_len):
                    ij = abs(arr[i] - arr[j])
                    jk = abs(arr[j] - arr[k])
                    ik = abs(arr[i] - arr[k])
                    if ij <= a and jk <= b and ik <= c:
                        ans += 1
        return ans


if __name__ == '__main__':
    arr = [3, 0, 1, 1, 9, 7]
    a, b, c = 7, 2, 3
    ans = Solution().countGoodTriplets(arr, a, b, c)
    print(ans)
