# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 二叉搜索树, 中序遍历
    def isValidBST(self, root: TreeNode) -> bool:
        val = []

        def inorder(root):
            if root is None: return None

            inorder(root.left)
            val.append(root.val)
            inorder(root.right)

        inorder(root)

        val_sort = sorted(val)
        for k in range(0, len(val) - 1):
            if val_sort[k] == val_sort[k + 1]:
                return False
        if val == val_sort:
            return True
        else:
            return False


if __name__ == '__main__':
    t1 = TreeNode(10)
    t2 = TreeNode(5)
    t3 = TreeNode(15)
    t4 = TreeNode(6)
    t5 = TreeNode(20)
    t1.left = t2
    t1.right = t3
    t3.left = t4
    t4.right = t5

    # t1 = TreeNode(2)
    # t2 = TreeNode(1)
    # t3 = TreeNode(3)
    # t1.left = t2
    # t1.right = t3

    ans = Solution().isValidBST(t1)
    print('F: ', ans)
