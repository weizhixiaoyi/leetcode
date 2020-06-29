# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0

        def helper(root):
            if root is None: return 0

            left = helper(root.left)
            right = helper(root.right)
            self.ans = max(self.ans, left + right)
            # print(left, right)
            return max(left, right) + 1

        helper(root)
        return self.ans


if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    ans = Solution().diameterOfBinaryTree(t1)
    print('ans: ', ans)
