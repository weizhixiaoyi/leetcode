# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 栈来存储函数的调用
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None: return 0

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        if root.left is None or root.right is None:
            return left + right + 1
        return min(left, right) + 1

    # def postOrder(self, root):
    #     if root is None: return None
    #
    #     self.postOrder(root.left)
    #     self.postOrder(root.right)
    #     print(root.val, end = ' ')


if __name__ == '__main__':
    t1 = TreeNode(3)
    t2 = TreeNode(9)
    t3 = TreeNode(20)
    t4 = TreeNode(15)
    t5 = TreeNode(7)
    t1.left = t2
    t1.right = t3
    t3.left = t4
    t3.right = t5
    ans = Solution().minDepth(t1)
    print('F: ', ans)
    # Solution().postOrder(t1)
