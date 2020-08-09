# -*- coding:utf-8 -*-

class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.strip().split()
        s_list.reverse()
        return ' '.join(s_list)


if __name__ == '__main__':
    s = "  a good   example  "
    ans = Solution().reverseWords(s)
    print(ans)
