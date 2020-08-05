# -*- coding:utf-8 -*-


from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 对数组进行反转
    """
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None: return []

        from queue import Queue
        q = Queue()
        q.put(root)
        nums, num = [], []

        flag = True
        while not q.empty():
            count = q.qsize()
            while count:
                cur = q.get()
                num.append(cur.val)
                if cur.left:
                    q.put(cur.left)
                if cur.right:
                    q.put(cur.right)
                count -= 1

            if flag is True:
                nums.append(num)
                num = []
                flag = False
            else:
                nums.append(list(reversed(num)))
                num = []
                flag = True
        # print(nums)
        return nums
    """

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None: return []

        from collections import deque
        ans = []

        def helper(root, level):
            if level == len(ans):
                ans.append(deque([root.val]))
            else:
                if level % 2 == 0:
                    ans[level].append(root.val)
                else:
                    ans[level].appendleft(root.val)

            if root.left:
                helper(root.left, level + 1)
            if root.right:
                helper(root.right, level + 1)

        helper(root, 0)
        ans = [list(v) for v in ans]
        return ans


if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t3.right = t5
    ans = Solution().zigzagLevelOrder(t1)
    print(ans)
