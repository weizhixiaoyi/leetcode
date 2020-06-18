# -*- coding:utf-8 -*-

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        import copy
        paths, path = [], []

        def order(root):
            if root is None:
                return None

            path.append(root.val)
            order(root.left)
            order(root.right)

            if root.left is None and root.right is None:
                paths.append(copy.deepcopy(path))
            path.pop()

        order(root)
        paths = [[str(v) for v in path] for path in paths]
        paths = ['->'.join(path) for path in paths]
        return paths


if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(5)
    t1.left = t2
    t1.right = t3
    t2.right = t4
    ans = Solution().binaryTreePaths(t1)
    print(ans)
