# -*- coding:utf-8 -*-
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from queue import Queue


def printLevelTree(root):
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        tree_len = len(postorder)

        def helper(in_left, in_right, pos_idx):
            if in_left > in_right or pos_idx < 0: return

            root = TreeNode(postorder[pos_idx])
            k = 0
            for i in range(in_left, in_right + 1):
                if inorder[i] == postorder[pos_idx]:
                    k = i
                    break

            root.left = helper(in_left, k - 1, pos_idx - (in_right - k + 1))
            root.right = helper(k + 1, in_right, pos_idx - 1)
            return root

        ans = helper(0, tree_len - 1, tree_len - 1)
        return ans


if __name__ == '__main__':
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    ans = Solution().buildTree(inorder, postorder)
    printLevelTree(ans)
