# -*- coding:utf-8 -*-

class Solution:
    def countDigitOne(self, n: int) -> int:
        digit, res = 1, 0

        # 2304; high = 23, cur = 0, low = 4
        high, cur, low = n // 10, n % 10, 0
        while high != 0 or cur != 0:
            if cur == 0:
                res += high * digit
            elif cur == 1:
                res += high * digit + low + 1
            else:
                res += (high + 1) * digit

            low += (cur * digit)
            cur = high % 10
            high = high // 10
            digit = digit * 10
        return res


if __name__ == '__main__':
    n = 12
    ans = Solution().countDigitOne(n)
    print(ans)
