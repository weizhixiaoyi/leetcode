# -*- coding:utf-8 -*-
from typing import List


class Solution:
    """
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        words_len = len(words)

        for i in range(words_len):
            for j in range(words_len):
                if i == j: continue
                cur_s = words[i] + words[j]
                cur_flag = self.par(cur_s)
                if cur_flag:
                    ans.append([i, j])
        return ans

    def par(self, cur_s):
        cur_len = len(cur_s)
        l, r = 0, cur_len - 1
        while l <= r:
            if cur_s[l] != cur_s[r]:
                return False
            l += 1
            r -= 1
        return True
    """

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        words_len = len(words)

        rev_words_dict = {}
        for i, word in enumerate(words):
            rev_word = word[::-1]
            rev_words_dict[rev_word] = i
        # print(rev_words_set)

        ans = []
        for i, word in enumerate(words):
            word_len = len(word)
            for k in range(0, word_len + 1):
                if self.par(word[k:]) and word[:k] in rev_words_dict:
                    j = rev_words_dict[word[:k]]
                    if i != j: ans.append([i, j])

                if self.par(word[:k]) and word[k:] in rev_words_dict:
                    j = rev_words_dict[word[k:]]
                    if i != j: ans.append([j, i])

        ans = list(set(tuple(val) for val in ans))
        ans = [list(val) for val in ans]
        return ans

    def par(self, cur_s):
        cur_len = len(cur_s)
        l, r = 0, cur_len - 1
        while l <= r:
            if cur_s[l] != cur_s[r]:
                return False
            l += 1
            r -= 1
        return True


if __name__ == '__main__':
    # words = ["abcd", "dcba", "lls", "s", "sssll"]
    # words = ['a', '']
    words = ["a", "abc", "aba", ""]
    ans = Solution().palindromePairs(words)
    print(ans)
    # print(Solution().par('aba'))
