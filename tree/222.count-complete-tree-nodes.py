# -*- coding:utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # def countNodes(self, root: TreeNode) -> int:
    #     ans = [0]
    #

    # def helper(root):
    #     if root is None:
    #         return None
    #
    #     helper(root.left)
    #     ans[0] += 1
    #     helper(root.right)
    #
    # helper(root)
    # return ans[0]

    import functools
    functools.lru_cache(None)

    def countNodes(self, root: TreeNode) -> int:
        if root is None: return 0
        # return self.countNodes(root.left) + self.countNodes(root.right) + 1

        left = self.countNodes(root.left) + 1
        right = self.countNodes(root.right)

        return left + right


if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6

    ans = Solution().countNodes(t1)
    print('ans: ', ans)
