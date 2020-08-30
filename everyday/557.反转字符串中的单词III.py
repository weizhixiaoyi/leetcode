# -*- coding:utf-8 -*-

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        for i in range(len(s)):
            s[i] = s[i][::-1]
        return ' '.join(s)


if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    ans = Solution().reverseWords(s)
    print(ans)
