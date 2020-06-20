# -*- coding:utf-8 -*-

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None: return []
        from queue import Queue
        ans = []
        q = Queue()
        q.put(root)
        ans.append([root.val])
        while not q.empty():
            tl = []
            count = q.qsize()
            # print(count)
            while count:
                t = q.get()
                if t.left:
                    q.put(t.left)
                    tl.append(t.left.val)
                if t.right:
                    q.put(t.right)
                    tl.append(t.right.val)
                # print(t.val)
                count -= 1
            if tl:
                ans.append(tl)
        ans = [ans[k] for k in range(len(ans) - 1, -1, -1)]
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
    ans = Solution().levelOrderBottom(t1)
    print('ans: ', ans)
