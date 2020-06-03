# -*- coding:utf-8 -*-

from queue import Queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def build_tree_from_level_list(nums: list) -> TreeNode:
    if len(nums) == 0: return TreeNode(None)

    q = Queue()
    temp = TreeNode(nums[0])
    q.put(temp)
    del nums[0]
    root = temp
    while len(nums) != 0:
        temp = q.get()
        if len(nums) >= 1:
            temp.left = TreeNode(nums[0])
            q.put(root.left)
            del nums[0]
        if len(nums) >= 1:
            temp.right = TreeNode(nums[0])
            q.put(root.right)
            del nums[0]

    return root


def print_level_tree(root: TreeNode):
    if root.val is None: return None

    q = Queue()
    q.put(root)
    while not q.empty():
        cur = q.get()
        print(cur.val, end=" ")

        if cur.left is not None:
            q.put(cur.left)
        if cur.right is not None:
            q.put(cur.right)
    print()


# 可以不用传递list来实现传递引用的特性
# 也可通过在rangeSumBST中定义self.ans来保持定义全局变量方法
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def sumBST(root: TreeNode, L: int, R: int, sum: list) -> int:
            if root is None:
                return 0

            sumBST(root.left, L, R, sum)
            if root.val is not None and ((L < root.val < R) or (root.val == L) or (root.val == R)):
                sum[0] += root.val
                # print(sum[0])
            sumBST(root.right, L, R, sum)

        sum = [0]
        sumBST(root, L, R, sum)
        return sum[0]


if __name__ == '__main__':
    tree_val = [10, 5, 15, 3, 7, None, 18]
    root = build_tree_from_level_list(tree_val)
    print_level_tree(root)

    solution = Solution()
    L, R = 7, 15
    ans = solution.rangeSumBST(root, L, R)
    print('ans: ', ans)
