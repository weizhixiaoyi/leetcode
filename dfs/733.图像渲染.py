# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image: return []
        m, n = len(image), len(image[0])
        pre = image[sr][sc]
        if pre == newColor: return image
        dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

        def dfs(cur_x, cur_y):
            image[cur_x][cur_y] = newColor

            for k in range(4):
                new_x, new_y = cur_x + dx[k], cur_y + dy[k]
                if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n or image[new_x][new_y] != pre: continue

                dfs(new_x, new_y)

        dfs(sr, sc)
        return image


if __name__ == '__main__':
    # image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    # sr, sc, newColor = 1, 1, 2
    # image = [[0, 0, 0], [0, 1, 1]]
    # sr, sc, newColor = 1, 1, 1
    image = [[0, 0, 0], [0, 1, 0]]
    sr, sc, newColor = 1, 1, 2
    ans = Solution().floodFill(image, sr, sc, newColor)
    print(ans)
