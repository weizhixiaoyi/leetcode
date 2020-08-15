# -*- coding:utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 一个节点共两个子节点, 四个孙子节点
# 那么最大值为max(当前节点+四个孙子节点, 两个子节点)
class Solution:
    """
    def rob(self, root: TreeNode) -> int:
        self.dict = {}

        def dfs(root):
            if not root: return 0
            if id(root) in self.dict:
                return self.dict[id(root)]

            cur = root.val
            if root.left:
                cur += (dfs(root.left.left) + dfs(root.left.right))
            if root.right:
                cur += (dfs(root.right.left) + dfs(root.right.right))

            self.dict[id(root)] = max(cur, dfs(root.left) + dfs(root.right))
            return self.dict[id(root)]

            # return max(cur, dfs(root.left) + dfs(root.right))

        return dfs(root)
    """

    def rob(self, root: TreeNode) -> int:
        def dfs(root):
            if not root: return [0, 0]

            left = dfs(root.left)
            right = dfs(root.right)

            tmp = [0, 0]
            tmp[0] = max(left[0], left[1]) + max(right[0], right[1])
            tmp[1] = left[0] + right[0] + root.val
            return tmp

        ans = dfs(root)
        return max(ans[0], ans[1])


if __name__ == '__main__':
    # t1 = TreeNode(3)
    # t2 = TreeNode(4)
    # t3 = TreeNode(5)
    # t4 = TreeNode(1)
    # t5 = TreeNode(2)
    # t6 = TreeNode(1)
    # t1.left = t2
    # t1.right = t3
    # t2.left = t4
    # t2.right = t5
    # t3.right = t6

    t1 = TreeNode(3)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(3)
    t5 = TreeNode(1)
    t1.left = t2
    t1.right = t3
    t2.right = t4
    t3.right = t5
    ans = Solution().rob(t1)
    print(ans)

"""
nums = []
dfs(root, nums)
nums_len = len(nums)
dp = [0 for i in range(nums_len)]
if nums_len == 1: return nums[0]
if nums_len == 2: return max(nums[0], nums[1])

# print(nums)
dp[0] = nums[0]
dp[1] = max(nums[0], nums[1])
for i in range(2, nums_len):
    dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
# print(dp)
return dp[nums_len - 1]
"""
