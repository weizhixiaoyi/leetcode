# -*- coding:utf-8 -*-

from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        if not beginWord or not endWord or len(wordList) == 0: return 0

        wordLen = len(beginWord)
        # 学习使用defaultdict
        from collections import defaultdict
        diff = defaultdict(list)
        for word in wordList:
            for i in range(wordLen):
                diff[word[0:i] + "*" + word[i + 1:]].append(word)

        from queue import Queue
        q = Queue()
        # 整个路径寻找的过程可以看过从beginWord到endWord的一张图, 初始点层次为1
        q.put((beginWord, 1))
        visited = [beginWord]

        while not q.empty():
            cur = q.get()
            cur_word, cur_index = cur[0], cur[1]
            # print(cur_word)

            for i in range(0, wordLen):
                candidate_word = diff[cur_word[0:i] + "*" + cur_word[i + 1:]]
                for k in range(len(candidate_word)):
                    if candidate_word[k] == endWord:
                        return cur_index + 1

                    if candidate_word[k] not in visited:
                        q.put((candidate_word[k], cur_index + 1))
                        visited.append(candidate_word[k])
        return 0


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    ans = Solution().ladderLength(beginWord, endWord, wordList)
    print('ans: ', ans)
