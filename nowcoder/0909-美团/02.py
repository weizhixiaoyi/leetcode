# -*- coding:utf-8 -*-


class Solution:
    def solve(self, s):
        s_len = len(s)
        lower = 0
        for i in range(s_len):
            if s[i].islower():
                lower += 1

        biger = s_len - lower
        if lower == biger:
            return 0
        if lower > biger:
            lower, biger = biger, lower

        return (biger - lower) // 2


if __name__ == '__main__':
    s = input()
    ans = Solution().solve(s)
    print(ans)
