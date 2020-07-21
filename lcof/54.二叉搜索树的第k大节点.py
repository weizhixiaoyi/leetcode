# -*- coding:utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # def kthLargest(self, root: TreeNode, k: int) -> int:
    #     def helper(root):
    #         if root is None: return None
    #
    #         helper(root.left)
    #         nums.append(root.val)
    #         helper(root.right)
    #
    #     nums = []
    #     helper(root)
    #
    #     nums_len = len(nums)
    #     return nums[nums_len - k]

    def kthLargest(self, root: TreeNode, k: int) -> int:
        def helper(root):
            if root is None: return None

            helper(root.right)
            if self.k == 0: return None
            self.k -= 1
            if self.k == 0: self.ans = root.val

            helper(root.left)

        self.ans = 0
        self.k = k
        helper(root)
        return self.ans


if __name__ == '__main__':
    t1 = TreeNode(3)
    t2 = TreeNode(1)
    t3 = TreeNode(4)
    t4 = TreeNode(2)
    t1.left = t2
    t1.right = t3
    t2.right = t4
    k = 2
    ans = Solution().kthLargest(t1, k)
    print(ans)
