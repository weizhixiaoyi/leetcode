# -*- coding:utf-8 -*-

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        import copy
        self.paths, self.path = [], []
        self.cur_sum = 0

        def helper(root):
            if root is None: return None

            self.path.append(root.val)
            self.cur_sum += root.val
            if (self.cur_sum == sum) and (root and root.left is None and root.right is None):
                # print(self.cur_sum)
                # print(self.path)
                self.paths.append(copy.deepcopy(self.path))

            helper(root.left)
            helper(root.right)
            self.cur_sum -= root.val
            self.path.pop()

        helper(root)
        return self.paths


if __name__ == '__main__':
    t1 = TreeNode(5)
    t2 = TreeNode(4)
    t3 = TreeNode(8)
    t4 = TreeNode(11)
    t5 = TreeNode(13)
    t6 = TreeNode(4)
    t7 = TreeNode(7)
    t8 = TreeNode(2)
    t9 = TreeNode(5)
    t10 = TreeNode(1)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t3.left = t5
    t3.right = t6
    t4.left = t7
    t4.right = t8
    t6.left = t9
    t6.right = t10
    sum = 22
    F = Solution().pathSum(t1, sum)
    print('F: ', F)
