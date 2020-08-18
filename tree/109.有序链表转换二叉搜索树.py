# -*- coding:utf-8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head: return None
        nums = []
        tmp = head
        while tmp:
            nums.append(tmp.val)
            tmp = tmp.next

        def dfs(nums, l, r):
            if l > r: return None

            idx = (l + r) // 2
            root = TreeNode(nums[idx])
            left = dfs(nums, l, idx - 1)
            right = dfs(nums, idx + 1, r)
            root.left = left
            root.right = right
            return root

        ans = dfs(nums, 0, len(nums) - 1)
        return ans


if __name__ == '__main__':
    t1 = ListNode(-10)
    t2 = ListNode(3)
    t3 = ListNode(0)
    t4 = ListNode(9)
    t5 = ListNode(5)
    t1.next = t2
    t2.next = t3
    t3.next = t4
    t4.next = t5
    ans = Solution().sortedListToBST(t1)
    printLevelTree(ans)
