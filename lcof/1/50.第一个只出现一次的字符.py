# -*- coding:utf-8 -*-

class Solution:
    def firstUniqChar(self, s: str) -> str:
        if not s: return " "

        from collections import defaultdict
        char_dict = defaultdict(int)
        for c in s:
            char_dict[c] += 1
        for c in s:
            if char_dict[c] == 1:
                return c
        return " "



if __name__ == '__main__':
    s = "abaccdeff"
    ans = Solution().firstUniqChar(s)
    print(ans)
