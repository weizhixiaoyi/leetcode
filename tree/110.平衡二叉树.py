# -*- coding:utf-8 -*-


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        self.ans = True

        def helper(root):
            if not root: return 0

            l1 = helper(root.left)
            l2 = helper(root.right)

            if abs(l1 - l2) > 1:
                self.ans = False
            return max(l1, l2) + 1

        helper(root)
        return self.ans


if __name__ == '__main__':
    t1 = TreeNode(3)
    t2 = TreeNode(9)
    t3 = TreeNode(20)
    t4 = TreeNode(15)
    t5 = TreeNode(7)
    t6 = TreeNode(3)
    t1.left = t2
    t1.right = t3
    t3.left = t4
    t3.right = t5
    t5.right = t6
    ans = Solution().isBalanced(t1)
    print(ans)
