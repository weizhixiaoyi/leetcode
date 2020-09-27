# -*- coding:utf-8 -*-


import sys
sys.setrecursionlimit(1000000)
class Solution:
    def solve(self, n, k, values, huchi):
        huchi = set(huchi)

        self.max_score = 0

        def dfs(cur_node, cur_path, cur_k, cur_score):
            if cur_k == k:
                self.max_score = max(self.max_score, cur_score)
                return
            if cur_k > k:
                return

            for i in range(1, n + 1):
                if i in cur_path: continue
                if (cur_node, i) in huchi or (i, cur_node) in huchi: continue

                dfs(i, cur_path.append(i), cur_k + 1, cur_score + values[i - 1])

        for i in range(1, n + 1):
            dfs(i, [i], 1, values[i - 1])
        return self.max_score


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        values = list(map(int, input().split()))
        huchi = []
        for _ in range(n - 1):
            a, b = map(int, input().split())
            huchi.append((a, b))
        ans = Solution().solve(n, k, values, huchi)
        print(ans)

    # n, k = 5, 2
    # values = [2, 3, 1, 5, 4]
    # huchi = [
    #     (1, 2),
    #     (1, 3),
    #     (1, 4),
    #     (1, 5)
    # ]
    # ans = Solution().solve(n, k, values, huchi)
    # print(ans)