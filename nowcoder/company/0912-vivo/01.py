# -*- coding:utf-8 -*-


class Solution:
    def solve(self, position, grids, n):
        start_x, start_y, end_x, end_y = position
        if start_x < 0 or start_y >= n or end_x < 0 or end_y >= n: return -1
        if n <= 5: return -1
        if n >= 10000: return -1
        if grids[end_x][end_y] == '#' or grids[end_x][end_y] == '@': return -1

        # print(start_x, start_y, end_x, end_y)
        dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

        from queue import Queue
        q = Queue()
        q.put((start_x, start_y, 0))
        grids[start_x][start_y] = '#'

        while not q.empty():
            cur_x, cur_y, cur_level = q.get()
            if cur_x == end_x and cur_y == end_y:
                return cur_level
            for k in range(4):
                new_x, new_y = cur_x + dx[k], cur_y + dy[k]
                if new_x < 0 or new_x >= n or new_y < 0 or new_y >= n: continue
                if grids[new_x][new_y] == '#' or grids[new_x][new_y] == '@': continue
                q.put((new_x, new_y, cur_level + 1))
                grids[new_x][new_y] = '#'
        return -1


if __name__ == '__main__':
    n = int(input())
    position = list(map(int, input().split()))
    grids = []
    for i in range(n):
        line = input()
        line = [v for v in line]
        grids.append(line)
    ans = Solution().solve(position, grids, n)
    print(ans)
