# -*- coding:utf-8 -*-
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # def preorderTraversal(self, root: TreeNode) -> List[int]:
    #     self.ans = []
    #
    #     def helper(root):
    #         if root is None: return None
    #
    #         self.ans.append(root.val)
    #         helper(root.left)
    #         helper(root.right)
    #
    #     helper(root)
    #     return self.ans

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None: return []

        ans = []
        stack = []
        while root or stack:
            while root:
                ans.append(root.val)
                stack.append(root)
                root = root.left

            cur = stack.pop()
            root = cur.right
        return ans


if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t1.right = t2
    t2.left = t3
    ans = Solution().preorderTraversal(t1)
    print(ans)
