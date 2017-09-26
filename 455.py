#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g, s = sorted(g), sorted(s)
        res = 0
        while g and s:
            if s[0] < g[0]:
                del s[0]
            else:
                res += 1
                del s[0]
                del g[0]
        return res

print(Solution().findContentChildren([1,2,3],[1,1]))