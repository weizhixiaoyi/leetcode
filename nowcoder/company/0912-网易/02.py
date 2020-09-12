# -*- coding:utf-8 -*-


class Solution:
    def solve(self, s):
        if not s: return 0
        s_len = len(s)

        ans = 0
        for i in range(s_len - 1):
            # 以i为中心扩展
            ans += self.isPar(s, s_len, i, i)

            # 以i + 1为中心扩展
            ans += self.isPar(s, s_len, i, i + 1)
        return ans

    def isPar(self, s, s_len, left, right):
        while left >= 0 and right < s_len and s[left] == s[right]:
            left -= 1
            right += 1

        cur_len = right - left - 1
        if cur_len == 1: return 0
        return cur_len // 2


if __name__ == '__main__':
    s = input()
    ans = Solution().solve(s)
    print(ans)
