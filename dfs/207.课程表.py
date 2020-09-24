# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        relations = defaultdict(list)
        for prerequisite in prerequisites:
            l1, l2 = prerequisite
            relations[l1].append(l2)




if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[1, 0]]
    ans = Solution().canFinish(numCourses, prerequisites)
    print(ans)
