# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if root is None: return 0

        self.ans = 0

        # 针对下面两个节点回归到顶节点可采用后序遍历
        def helper(root):
            # 递归截止条件
            if root is None: return 0

            left = helper(root.left)
            right = helper(root.right)
            if (root.left is not None) and (root.val == root.left.val):
                left += 1
            else:
                left = 0
            if (root.right is not None) and (root.val == root.right.val):
                right += 1
            else:
                right = 0

            self.ans = max(self.ans, left + right)
            return max(left, right)

        helper(root)
        return self.ans


if __name__ == '__main__':
    t1 = TreeNode(5)
    t2 = TreeNode(4)
    t3 = TreeNode(5)
    t4 = TreeNode(1)
    t5 = TreeNode(1)
    t6 = TreeNode(5)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.right = t6

    ans = Solution().longestUnivaluePath(t1)
    print(ans)
