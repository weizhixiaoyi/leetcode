# -*- coding:utf-8 -*-
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if root is None: return []

        ans = []
        from queue import Queue
        q = Queue()
        q.put(root)

        while not q.empty():
            cur = q.get()
            ans.append(cur.val)
            if cur.left:
                q.put(cur.left)
            if cur.right:
                q.put(cur.right)

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
