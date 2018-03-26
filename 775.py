#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution:
    def isIdealPermutation(self, A):
        cmax = 0
        for i in range(len(A) - 2):
            cmax = max(cmax, A[i])
            if cmax > A[i + 2]:
                return False
        return True

print(Solution().isIdealPermutation([1,0,3]))
