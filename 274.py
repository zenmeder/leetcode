#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        citations = sorted(citations, reverse=True)
        n, res = len(citations), 0
        for i in range(n):
            if i >= citations[i]:
                return i
        return n
# print(Solution().hIndex([3, 0, 6, 1, 5]))
print(Solution().hIndex([0,1,0]))