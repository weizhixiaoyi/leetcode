# -*- coding:utf-8 -*-
from queue import Queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def build_tree_from_level_list(nums: list):
    if not nums: return TreeNode(None)

    q = Queue()
    root = TreeNode(nums[0])
    q.put(root)
    del nums[0]

    while nums:
        cur = q.get()

        if len(nums) >= 1:
            cur.left = TreeNode(nums[0])
            q.put(cur.left)
            del nums[0]

        if len(nums) >= 1:
            cur.right = TreeNode(nums[0])
            q.put(cur.right)
            del nums[0]
    return root


def print_level_tree(root: TreeNode):
    if root is None: return None

    q = Queue()
    q.put(root)
    while not q.empty():
        cur = q.get()
        print(cur.val, end=" ")

        if cur.left:
            q.put(cur.left)
        if cur.right:
            q.put(cur.right)
    print()


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        if root is None: return 0

        nums = []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            cur = stack.pop()
            if cur.val is not None:
                nums.append(cur.val)
            root = cur.right

        res = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
        min_value = min(res)
        return min_value


if __name__ == '__main__':
    tree_val = [1, 0, 48, None, None, 12, 49, None, None, None, None]
    root = build_tree_from_level_list(tree_val)
    print_level_tree(root)

    solution = Solution()
    ans = solution.minDiffInBST(root)
    print(ans)
