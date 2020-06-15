# -*- coding:utf-8 -*-

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, 50000
        while left <= right:
            mid = left + (right - left) // 2
            cur_num = mid * mid
            if cur_num == num:
                return True
            if cur_num < num:
                left = mid + 1
            if cur_num > num:
                right = mid - 1
        return False


if __name__ == '__main__':
    num = 2
    ans = Solution().isPerfectSquare(num)
    print(ans)
