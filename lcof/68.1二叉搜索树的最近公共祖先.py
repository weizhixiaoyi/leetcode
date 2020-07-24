# -*- coding:utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = TreeNode(None)

        def helper(root, p, q):
            if root is None: return False

            left = helper(root.left, p, q)
            right = helper(root.right, p, q)

            equal = False
            if root == p or root == q:
                equal = True
            if (left and right) or (left and equal) or (right and equal):
                self.res = root

            return left or right or equal

        helper(root, p, q)
        return self.res
    """
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                break
        return root
    """

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root


if __name__ == '__main__':
    t1 = TreeNode(6)
    t2 = TreeNode(2)
    t3 = TreeNode(8)
    t4 = TreeNode(0)
    t5 = TreeNode(4)
    t6 = TreeNode(7)
    t7 = TreeNode(9)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    t3.right = t7
    ans = Solution().lowestCommonAncestor(t1, t4, t5)
    print(ans.val)
