# -*- coding:utf-8 -*-
from typing import List


class Solution:
    """
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        rooms_len = len(rooms)
        could = [False for i in range(rooms_len)]
        could[0] = True

        from queue import Queue
        q = Queue()
        for v in rooms[0]:
            q.put(v)

        while not q.empty():
            q_size = q.qsize()
            while q_size:
                cur = q.get()
                q_size -= 1
                if could[cur]:
                    continue
                could[cur] = True
                for v in rooms[cur]:
                    q.put(v)
        # print(could)
        if False in could:
            return False
        else:
            return True
    """

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        rooms_len = len(rooms)
        could = [True if i == 0 else False for i in range(rooms_len)]

        def dfs(idx, rooms, could, ans):
            if False not in could:
                ans[0] = True
                # return True

            for k in range(len(rooms[idx])):
                if could[rooms[idx][k]]: continue
                could[rooms[idx][k]] = True
                dfs(rooms[idx][k], rooms, could, ans)
                # could[rooms[idx][k]] = False

        ans = [False]
        dfs(0, rooms, could, ans)
        return ans[0]


if __name__ == '__main__':
    # rooms = [[1], [2], [3], []]
    rooms = [[1, 3], [3, 0, 1], [2], [0]]
    # rooms = [[2, 3], [], [2], [1, 3, 1]]
    ans = Solution().canVisitAllRooms(rooms)
    print(ans)
