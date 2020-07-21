# -*- coding:utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None: return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1


if __name__ == '__main__':
    t1 = TreeNode(3)
    t2 = TreeNode(1)
    t3 = TreeNode(4)
    t4 = TreeNode(2)
    t1.left = t2
    t1.right = t3
    t2.right = t4
    ans = Solution().maxDepth(t1)
    print(ans)
