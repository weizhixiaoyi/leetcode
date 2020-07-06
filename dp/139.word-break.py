# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(s) == 0 and len(wordDict) == 0: return True
        if len(s) == 0 and len(wordDict) != 0: return False
        if len(s) != 0 and len(wordDict) == 0: return False

        from collections import defaultdict
        # 以char开头的单词
        char2word = defaultdict(list)
        for word in wordDict:
            char2word[word[0]].append(word)

        self.flag = False

        import functools
        @functools.lru_cache(None)
        def helper(s):
            # 递归截止条件
            # 能够找到真正的答案
            if len(s) == 0:
                return True
            # s非空且再也找不到答案
            if len(char2word[s[0]]) == 0:
                return False

            # 针对以char开头的字符和现有字符串是否匹配
            candidate_word = char2word[s[0]]
            cur_s_len = len(s)
            for cw in candidate_word:
                cw_len = len(cw)
                if cw_len <= cur_s_len and cw == s[0:cw_len]:
                    if helper(s[cw_len:]):
                        self.flag = True

            return False

        helper(s)
        return self.flag


if __name__ == '__main__':
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
    ans = Solution().wordBreak(s, wordDict)
    print(ans)
