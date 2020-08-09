# -*- coding:utf-8 -*-

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(n):
            if n == 0:
                return 1

            y = helper(n // 2)
            if n % 2 == 0:
                ans = y * y
            else:
                ans = y * y * x
            return ans

        return helper(n) if n >= 0 else 1 / helper(-n)


if __name__ == '__main__':
    x, n = 2.10000, 3
    # x, n = 0.00001, 2147483647
    # x, n = -1.00001, 447125
    ans = Solution().myPow(x, n)
    print(ans)
