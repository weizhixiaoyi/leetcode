# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degrees = dict((u, 0) for u in range(numCourses))
        adajacency = dict((u, []) for u in range(numCourses))
        for cur, pre in prerequisites:
            in_degrees[cur] += 1
            adajacency[pre].append(cur)

        ans = []
        Q = [u for u in range(numCourses) if in_degrees[u] == 0]
        while Q:
            u = Q.pop()
            ans.append(u)
            for v in adajacency[u]:
                in_degrees[v] -= 1
                if in_degrees[v] == 0:
                    Q.append(v)
        if len(ans) == numCourses:
            return ans
        else:
            return []


if __name__ == '__main__':
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    # numCourses = 2
    # prerequisites = [[1, 0]]
    ans = Solution().findOrder(numCourses, prerequisites)
    print(ans)
