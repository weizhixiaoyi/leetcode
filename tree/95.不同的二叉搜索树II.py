# -*- coding:utf-8 -*-
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0: return []

        def dfs(l, r):
            if l > r: return [None]
            if l == r: return [TreeNode(l)]

            ans = []
            for i in range(l, r + 1):
                # 已经保证是符合二叉搜索树
                left_list = dfs(l, i - 1)
                right_list = dfs(i + 1, r)
                for left in left_list:
                    for right in right_list:
                        # if left and right and left.val < root.val < right.val:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        ans.append(root)
            return ans

        ans = dfs(1, n)
        # print(len(ans))
        # for a in ans:
        #     printLevelTree(a)

        return ans


if __name__ == '__main__':
    n = 3
    ans = Solution().generateTrees(n)
    print(ans)
