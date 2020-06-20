# -*- coding:utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.n = 0
        self.ans = 0

        def helper(root):
            if root is None: return None

            helper(root.left)
            self.n += 1
            if self.n == k:
                self.ans = root.val
            helper(root.right)

        helper(root)
        return self.ans


if __name__ == '__main__':
    t1 = TreeNode(3)
    t2 = TreeNode(1)
    t3 = TreeNode(4)
    t4 = TreeNode(2)
    t1.left = t2
    t1.right = t3
    t2.right = t4
    k = 4
    ans = Solution().kthSmallest(t1, k)
    print('ans: ', ans)
