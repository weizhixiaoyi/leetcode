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
    def inorder(self, root: TreeNode):
        if root is None:
            return None

        self.inorder(root.left)
        print(root.val, end=" ")
        self.inorder(root.right)

    def inorder_stack(self, root: TreeNode):
        if root is None:
            return False

        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            cur = stack.pop()
            print(cur.val, end=" ")
            root = cur.right


if __name__ == '__main__':
    tree_val = [10, 5, 15, 3, 7, None, 18]
    root = build_tree_from_level_list(tree_val)
    print_level_tree(root)
