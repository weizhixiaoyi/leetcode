# -*- coding:utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def printOrderTree(root):
    if not root: return None

    printOrderTree(root.left)
    print(root.val)
    printOrderTree(root.right)


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.root_sum = 0
        self.getSum(root)

        self.cur_sum = 0
        self.convert(root, 0)
        return root

    def convert(self, root, cur_sum):
        if not root: return None

        self.convert(root.left, cur_sum)
        tmp = root.val
        root.val = self.root_sum - self.cur_sum
        self.cur_sum += tmp
        self.convert(root.right, cur_sum)

    def getSum(self, root):
        if not root: return None

        self.getSum(root.left)
        self.root_sum += root.val
        self.getSum(root.right)


if __name__ == '__main__':
    t1 = TreeNode(5)
    t2 = TreeNode(2)
    t3 = TreeNode(13)
    t1.left = t2
    t1.right = t3
    ans = Solution().convertBST(t1)
    printOrderTree(ans)
