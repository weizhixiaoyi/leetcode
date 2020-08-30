# -*- coding:utf-8 -*-

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        s_rev = s[::-1]
        for i in range(len(s_rev)):
            # cur = s_rev[:i] + s
            # if self.isPar(cur):
            #     return cur
            if s.startswith(s_rev[i:]):
                return s_rev[:i] + s

    def isPar(self, s):
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True


if __name__ == '__main__':
    # s = "aacecaaa"
    s = "abcd"
    ans = Solution().shortestPalindrome(s)
    print(ans)
