# -*- coding:utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        import copy
        self.paths, self.path = [], []

        def helper(root):
            if root is None: return 0

            self.path.append(root.val)
            if root.left is None and root.right is None:
                self.paths.append(copy.deepcopy(self.path))

            helper(root.left)
            helper(root.right)
            self.path.pop()

        helper(root)
        # print(self.paths)
        ans = 0
        for path in self.paths:
            path_len = len(path)
            for k in range(0, path_len):
                ans += (path[k] * pow(10, path_len - k - 1))
        # print(ans)
        return ans


if __name__ == '__main__':
    t1 = TreeNode(4)
    t2 = TreeNode(9)
    t3 = TreeNode(0)
    t4 = TreeNode(5)
    t5 = TreeNode(1)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    ans = Solution().sumNumbers(t1)
    print('ans: ', ans)
