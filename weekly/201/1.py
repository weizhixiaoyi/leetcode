# -*- coding:utf-8 -*-

class Solution:
    def makeGood(self, s: str) -> str:
        while True:
            flag = False
            s_len = len(s)
            if s_len == 0: return ''
            for i in range(s_len - 1):
                if 'a' <= s[i] <= 'z' and 'A' <= s[i + 1] <= 'Z' and s[i] == s[i + 1].lower():
                    s = s.replace(s[i] + s[i + 1], '')
                    flag = True
                    break
                if 'A' <= s[i] <= 'Z' and 'a' <= s[i + 1] <= 'z' and s[i].lower() == s[i + 1]:
                    s = s.replace(s[i] + s[i + 1], '')
                    flag = True
                    break
            if not flag:
                return s


if __name__ == '__main__':
    s = "leEeetcode"
    # s = "abBAcC"
    ans = Solution().makeGood(s)
    print(ans)
