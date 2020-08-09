# -*- coding:utf-8 -*-
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum_value: int) -> List[List[int]]:
        if root is None: return []

        from copy import deepcopy
        self.paths, self.path = [], []

        def helper(root, sum_value):
            if root is None:
                return None

            self.path.append(root.val)
            helper(root.left, sum_value)
            helper(root.right, sum_value)
            if sum(self.path) == sum_value and root.left is None and root.right is None:
                self.paths.append(deepcopy(self.path))

            self.path.pop()

        helper(root, sum_value)
        return self.paths


if __name__ == '__main__':
    # t1 = TreeNode(5)
    # t2 = TreeNode(4)
    # t3 = TreeNode(8)
    # t4 = TreeNode(11)
    # t5 = TreeNode(13)
    # t6 = TreeNode(4)
    # t7 = TreeNode(7)
    # t8 = TreeNode(2)
    # t9 = TreeNode(5)
    # t10 = TreeNode(1)
    # t1.left = t2
    # t1.right = t3
    # t2.left = t4
    # t3.left = t5
    # t3.right = t6
    # t4.left = t7
    # t4.right = t8
    # t6.left = t9
    # t6.right = t10
    # sum_value = 22

    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t1.left = t2
    sum_value = 1
    ans = Solution().pathSum(t1, sum_value)
    print(ans)
