# -*- coding:utf-8 -*-


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q: return True
        if not p or not q: return False
        if p.val != q.val: return False

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        if left and right:
            return True
        return False


if __name__ == '__main__':
    t11 = TreeNode(1)
    t12 = TreeNode(2)
    t13 = TreeNode(3)
    t11.left = t12
    t11.right = t13

    t21 = TreeNode(1)
    t22 = TreeNode(2)
    t23 = TreeNode(3)
    t21.left = t22
    t21.right = t23

    ans = Solution().isSameTree(t11, t21)
    print(ans)
