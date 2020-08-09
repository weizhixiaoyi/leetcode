# -*- coding:utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        def helper(root):
            if root is None: return None

            helper(root.left)
            helper(root.right)

            temp = root.left
            root.left = root.right
            root.right = temp

        ans = root
        helper(root)
        return ans


if __name__ == '__main__':
    t1 = TreeNode(4)
    t2 = TreeNode(2)
    t3 = TreeNode(7)
    t4 = TreeNode(1)
    t5 = TreeNode(3)
    t6 = TreeNode(6)
    t7 = TreeNode(9)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    t3.right = t7
    ans = Solution().mirrorTree(t1)
