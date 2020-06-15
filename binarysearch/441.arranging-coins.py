# -*- coding:utf-8 -*-

class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, 70000
        while left <= right:
            mid = left + (right - left) // 2
            nums_mid = ((1 + mid) * mid) // 2
            # print(nums_mid)
            if nums_mid < n:
                left = mid + 1
            if nums_mid > n:
                right = mid - 1
            if nums_mid == n:
                return mid
        return left - 1


if __name__ == '__main__':
    s = Solution()
    n = 6
    ans = s.arrangeCoins(n)
    print(ans)
