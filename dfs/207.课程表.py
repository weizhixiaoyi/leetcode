# -*- coding:utf-8 -*-
from typing import List


class Solution:
    # 判断图中是否有环, 可采用拓扑排序进行实现
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degrees = dict((u, 0) for u in range(numCourses))
        adjacency = dict((u, []) for u in range(numCourses))
        for cur, pre in prerequisites:
            in_degrees[cur] += 1
            adjacency[pre].append(cur)
        # print(in_degrees, adjacency)

        ans = []
        Q = [v for v in in_degrees if in_degrees[v] == 0]
        while Q:
            u = Q.pop()
            ans.append(u)
            for v in adjacency[u]:
                in_degrees[v] -= 1
                if in_degrees[v] == 0:
                    Q.append(v)
        if len(ans) == numCourses:
            return True
        else:
            return False


if __name__ == '__main__':
    numCourses = 2
    # prerequisites = [[1, 0]]
    prerequisites = [[1, 0], [0, 1]]

    ans = Solution().canFinish(numCourses, prerequisites)
    print(ans)
