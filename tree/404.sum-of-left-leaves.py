# -*- coding:utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        # 如果是只有一个变量且想要全局共享, 则可利用self.***来保存变量
        self.res = 0

        def helper(root):
            if root is None: return None

            helper(root.left)
            helper(root.right)

            # 想到了此种判断的方法, 但没有理清数据返回的方式, 所以可以不用返回, 直接利用全局变量
            if root.left and (root.left.left is None and root.left.right is None):
                self.res += root.left.val

        helper(root)
        return self.res


if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    ans = Solution().sumOfLeftLeaves(t1)
    print('F: ', ans)
