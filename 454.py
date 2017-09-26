#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
import collections
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        AB = collections.Counter(a + b for a in A for b in B)
        return sum(AB[-c - d] for c in C for d in D)


print(Solution().fourSumCount([0,1,-1]
,[-1,1,0]
,[0,0,1]
,[-1,1,1]))
