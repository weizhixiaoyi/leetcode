# -*- coding:utf-8 -*-

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len, t_len = len(s), len(t)
        if s_len > t_len: return False
        if s_len == t_len and s != t: return False

        i, j = 0, 0
        while i < s_len and j < t_len:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        if i == s_len:
            return True
        else:
            return False


if __name__ == '__main__':
    s = "abc"
    t = "ahbgdc"
    ans = Solution().isSubsequence(s, t)
    print(ans)
