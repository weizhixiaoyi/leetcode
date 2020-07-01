# -*- coding:utf-8 -*-

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None: return []
        from queue import Queue

        nums, num = [], []
        q = Queue()
        q.put(root)
        while not q.empty():
            count = q.qsize()
            while count:
                cur = q.get()
                num.append(cur.val)
                if cur.left:
                    q.put(cur.left)
                if cur.right:
                    q.put(cur.right)
                count -= 1

            nums.append(num)
            num = []

        ans = []
        for v in nums:
            ans.append(v[-1])
        return ans


if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    # t3 = TreeNode(3)
    # t4 = TreeNode(4)
    # t5 = TreeNode(5)
    t1.left = t2
    # t1.right = t3
    # t2.left = t4
    # t4.left = t5
    # t2.right = t5
    # t2.right = t5
    # t3.right = t4
    ans = Solution().rightSideView(t1)
    print(ans)
