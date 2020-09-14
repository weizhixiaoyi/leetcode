# -*- coding:utf-8 -*-

from typing import List


class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        ans = 0

        def unhappy(x, y):
            flag = 0
            for u in preferences[x]:
                if u == y: break
                if u != y:
                    for v in preferences[u]:
                        if [u, v] in pairs or [v, u] in pairs:
                            idx1 = preferences[u].index(x)
                            idx2 = preferences[u].index(v)
                            if idx1 < idx2:
                                flag = 1
                                break
                if flag:
                    break

            if flag:
                return True
            else:
                return False

        for pair in pairs:
            x, y = pair
            if unhappy(x, y):
                ans += 1
            if unhappy(y, x):
                ans += 1

        return ans


if __name__ == '__main__':
    # n = 4
    # preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]]
    # pairs = [[0, 1], [2, 3]]
    # n = 4
    # preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]]
    # pairs = [[1, 3], [0, 2]]
    n = 2
    preferences = [[1], [0]]
    pairs = [[1, 0]]
    # n = 4
    # preferences = [[1, 3, 2], [2, 3, 0], [1, 0, 3], [1, 0, 2]]
    # pairs = [[2, 1], [3, 0]]

    ans = Solution().unhappyFriends(n, preferences, pairs)
    print(ans)
