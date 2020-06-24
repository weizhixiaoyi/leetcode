# -*- coding:utf-8 -*-

class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, int(x ** 0.5) + 1
        while left <= right:
            mid = left + (right - left) // 2
            cur = mid * mid
            cur_add = (mid + 1) * (mid + 1)
            if cur <= x < cur_add:
                return mid
            if cur < x:
                left = mid + 1
            if cur_add > x:
                right = mid - 1


if __name__ == '__main__':
    x = 122
    ans = Solution().mySqrt(x)
    print('ans: ', ans)
