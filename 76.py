#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        def getLetter(s):
            cs = {}
            for i in range(len(s)):
                if s[i] in cs:
                    cs[s[i]].append(i)
                else:
                    cs[s[i]] = [i]
            return cs
        cs = getLetter(s)

print(Solution().minWindow('ADOBECODEBANC','ABC'))

