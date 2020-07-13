# -*- coding:utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None: return True

        def helper(root1, root2):
            if (root1 is None) and (root2 is None):
                return True
            if (root1 is None) or (root2 is None):
                return False
            if root1.val != root2.val:
                return False

            if helper(root1.left, root2.right) is False:
                return False
            if helper(root1.right, root2.left) is False:
                return False
            return True

        ans = helper(root, root)
        return ans


if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(2)
    t4 = TreeNode(3)
    t5 = TreeNode(4)
    t6 = TreeNode(4)
    t7 = TreeNode(3)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    t3.right = t7
    ans = Solution().isSymmetric(t1)
    print(ans)
