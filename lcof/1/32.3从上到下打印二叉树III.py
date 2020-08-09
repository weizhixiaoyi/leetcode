## -*- coding:utf-8 -*-
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None: return []

        ans = []
        from collections import deque
        q = deque()
        q.append(root)

        while len(q) != 0:
            level = deque()
            count = len(q)
            while count:
                cur = q.popleft()
                if len(ans) % 2 == 0:
                    level.append(cur.val)
                else:
                    level.appendleft(cur.val)

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                count -= 1
            ans.append(list(level))

        return ans


if __name__ == '__main__':
    t1 = TreeNode(3)
    t2 = TreeNode(9)
    t3 = TreeNode(20)
    t4 = TreeNode(15)
    t5 = TreeNode(7)
    t1.left = t2
    t1.right = t3
    t3.left = t4
    t3.right = t5
    ans = Solution().levelOrder(t1)
    print(ans)
