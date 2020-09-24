# -*- coding:utf-8 -*-


class Solution:
    def solve(self, m, n):
        import math
        m_f = math.factorial(m)
        n_f = math.factorial(n)
        mn_f = math.factorial(m - n)
        return m_f // (n_f * mn_f)


if __name__ == '__main__':
    m = int(input())
    n = int(input())
    # m, n = 4, 2
    ans = Solution().solve(m, n)
    print(ans)
