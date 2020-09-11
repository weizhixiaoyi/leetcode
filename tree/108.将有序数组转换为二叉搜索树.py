# -*- coding:utf-8 -*-
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def printTree(root):
    from queue import Queue
    q = Queue()
    q.put(root)

    while not q.empty():
        q_size = q.qsize()
        value = []
        while q_size:
            cur = q.get()
            value.append(cur.val)
            if cur.left:
                q.put(cur.left)
            if cur.right:
                q.put(cur.right)
            q_size -= 1
        print(value)


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums: return None

        half = len(nums) // 2
        root = TreeNode(nums[half])
        root.left = self.sortedArrayToBST(nums[:half])
        root.right = self.sortedArrayToBST(nums[half + 1:])
        return root


if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9]
    ans = Solution().sortedArrayToBST(nums)
    printTree(ans)
