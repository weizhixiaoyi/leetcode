# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        k = m + n - 1
        i, j = m - 1, n - 1
        while i >= 0 and j >= 0:
            if A[i] >= B[j]:
                A[k] = A[i]
                i -= 1
                k -= 1
            else:
                A[k] = B[j]
                j -= 1
                k -= 1
        while i >= 0:
            A[k] = A[i]
            i -= 1
            k -= 1
        while j >= 0:
            A[k] = B[j]
            j -= 1
            k -= 1
