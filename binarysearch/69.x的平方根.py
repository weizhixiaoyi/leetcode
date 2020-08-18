# -*- coding:utf-8 -*-

class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left < right:
            mid = (left + right + 1) // 2
            cur_value = mid ** 2
            # print(mid)
            if cur_value > x:
                right = mid - 1
            else:
                left = mid
        return left


if __name__ == '__main__':
    x = 0
    ans = Solution().mySqrt(x)
    print(ans)
