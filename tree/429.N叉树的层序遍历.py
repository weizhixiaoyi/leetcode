# -*- coding:utf-8 -*-
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None: return []

        from queue import Queue
        q = Queue()
        q.put(root)
        ans = []
        while not q.empty():
            q_size = q.qsize()
            cur_ans = []
            while q_size:
                cur = q.get()
                cur_ans.append(cur.val)
                for ch in cur.children:
                    q.put(ch)
                q_size -= 1
            ans.append(cur_ans)
        return ans
