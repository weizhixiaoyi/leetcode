# -*- coding:utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.max_sum = float('-inf')

    def maxPathSum(self, root: TreeNode) -> int:
        def helper(root):
            if root is None: return 0

            left = helper(root.left)
            if left < 0: left = 0
            right = helper(root.right)
            if right < 0: right = 0
            cur_sum = root.val + left + right
            self.max_sum = max(self.max_sum, cur_sum)

            # 选择最大的一条路径值, 而非self.max_sum值
            return root.val + max(left, right)

        helper(root)
        return int(self.max_sum)


if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    # t3 = TreeNode(20)
    # t4 = TreeNode(15)
    # t5 = TreeNode(7)
    t1.left = t2
    # t1.right = t3
    # t3.left = t4
    # t3.right = t5
    ans = Solution().maxPathSum(t1)
    print(ans)
