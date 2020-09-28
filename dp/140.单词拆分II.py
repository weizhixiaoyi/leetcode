# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        from collections import defaultdict
        char2word = defaultdict(list)
        for word in wordDict:
            char2word[word[0]].append(word)
        # print(char2word)

        self.ans = []

        def dfs(cur_s, path):
            if len(cur_s) == 0:
                self.ans.append(' '.join(path))
                return
            if cur_s[0] not in char2word:
                return

            candidate = char2word[cur_s[0]]
            cur_s_len = len(cur_s)
            for c in candidate:
                c_len = len(c)
                if c_len <= cur_s_len and c == cur_s[0: c_len]:
                    dfs(cur_s[c_len:], path + [c])

        dfs(s, [])
        return self.ans


if __name__ == '__main__':
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    # s = "catsandog"
    # wordDict = ["cats", "dog", "sand", "and", "cat"]
    # s = "pineapplepenapple"
    # wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    ans = Solution().wordBreak(s, wordDict)
    print(ans)
