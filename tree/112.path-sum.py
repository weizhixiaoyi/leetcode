# -*- coding:utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        self.cur_sum = 0
        self.flag = False

        def helper(root):
            if root is None: return None

            self.cur_sum = self.cur_sum + root.val
            # 判断是否真正处于根节点
            if (self.cur_sum == sum) and (root is not None and root.left is None and root.right is None):
                # print(self.cur_sum, sum)
                self.flag = True

            helper(root.left)
            helper(root.right)
            self.cur_sum -= root.val

        helper(root)
        return self.flag


if __name__ == '__main__':
    t1 = TreeNode(5)
    t2 = TreeNode(4)
    # t3 = TreeNode(8)
    # t4 = TreeNode(11)
    # t5 = TreeNode(13)
    # t6 = TreeNode(4)
    t1.left = t2
    # t1.right = t3
    # t2.left = t4
    # t3.left = t5
    # t3.right = t6
    sum = 9
    F = Solution().hasPathSum(t1, sum)
    print('F: ', F)
