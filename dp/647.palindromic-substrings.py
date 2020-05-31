# -*- coding:utf-8 -*-

"""
判断以s[i]和s[i-1: i]为中心的字符串共有多少
"""


class Solution:
    import functools
    @functools.lru_cache(None)
    def countSubstrings(self, s: str) -> int:
        # 第一个字符串本身是回文串
        ans = 1
        for i in range(1, len(s)):
            #  当前字符本身是回文串
            # ans += 1

            #  当前字符与上一个字符能够构成回文串
            # if s[i] == s[i - 1]:
            #     ans += 1

            # 判断以s[i]为中心有多少回文串
            ans += self.expandString(s, i, i)

            # 判断以s[i-1: i]为中心有多少回文串
            ans += self.expandString(s, i - 1, i)
        return ans

    def expandString(self, s: str, l: int, r: int) -> int:
        cur_ans = 0
        while (l >= 0 and r < len(s) and s[l] == s[r]):
            cur_ans += 1
            l -= 1
            r += 1
        return cur_ans


if __name__ == '__main__':
    while True:
        try:
            s = input()
            solution = Solution()
            ans = solution.countSubstrings(s)
            print('ans: ', ans)
        except:
            break
