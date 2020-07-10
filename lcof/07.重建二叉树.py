# -*- coding:utf-8 -*-
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def printLevelTree(root):
    from queue import Queue
    q = Queue()
    q.put(root)
    while not q.empty():
        cur = q.get()
        print(cur.val, end=' ')
        if cur.left:
            q.put(cur.left)
        if cur.right:
            q.put(cur.right)

    print()


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(pre_root_idx, in_left_idx, in_right_idx):
            if in_left_idx > in_right_idx:
                return None

            root, k = None, 0
            for i in range(len(inorder)):
                if preorder[pre_root_idx] == inorder[i]:
                    root = TreeNode(preorder[pre_root_idx])
                    k = i
                    break

            root.left = helper(pre_root_idx + 1, in_left_idx, k - 1)
            root.right = helper(pre_root_idx + (k - in_left_idx + 1), k + 1, in_right_idx)
            return root

        tree = helper(0, 0, len(inorder) - 1)
        return tree


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    ans = Solution().buildTree(preorder, inorder)
    printLevelTree(ans)
