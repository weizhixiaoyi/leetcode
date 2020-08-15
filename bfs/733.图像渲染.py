# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image: return []
        m, n = len(image), len(image[0])

        dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
        from queue import Queue
        q = Queue()
        q.put((sr, sc))
        pre = image[sr][sc]
        if newColor == pre: return image
        image[sr][sc] = newColor

        while not q.empty():
            cur = q.get()
            cur_x, cur_y = cur[0], cur[1]
            for k in range(4):
                new_x, new_y = cur_x + dx[k], cur_y + dy[k]
                if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n: continue
                if image[new_x][new_y] != pre: continue

                image[new_x][new_y] = newColor
                q.put((new_x, new_y))

        return image


if __name__ == '__main__':
    # image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    # sr, sc, newColor = 1, 1, 2
    image = [[0, 0, 0], [0, 1, 1]]
    sr, sc, newColor = 1, 1, 1
    ans = Solution().floodFill(image, sr, sc, newColor)
    print(ans)
