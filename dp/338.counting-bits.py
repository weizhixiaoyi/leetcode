# -*- coding:utf-8 -*-

from typing import List
import pprint

"""
在pow(2, i)的二进制数中1的个数为1个
进而可以统计pow(2, i)到pow(2, i+1)个数内元素的数目
"""


class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0 for i in range(num + 1)]
        for i in range(0, 100):
            cur_value = pow(2, i)
            if cur_value <= num:
                dp[cur_value] = 1
        last = 0
        for i in range(2, num + 1):
            if dp[i] == 1:
                last = i
                pass
            dp[i] = dp[last] + dp[i - last]
        return dp


if __name__ == '__main__':
    while True:
        try:
            value = int(input())
            solution = Solution()
            ans = solution.countBits(value)
            print(ans)
        except:
            break
