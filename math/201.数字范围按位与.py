# -*- coding:utf-8 -*-

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == n: return m
        if m == 0: return 0

        def get_digit(num):
            for i in range(0, 32):
                if pow(2, i) <= num < pow(2, i + 1):
                    return i

        m_digit, n_digit = get_digit(m), get_digit(n)
        if m_digit != n_digit:
            return 0

        ans = m
        for k in range(m + 1, n + 1):
            ans = ans & k
            if ans == pow(2, m_digit):
                return ans
        return ans


if __name__ == '__main__':
    m = 0
    n = 1
    ans = Solution().rangeBitwiseAnd(m, n)
    print(ans)
