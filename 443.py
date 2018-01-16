#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        pre, res, length = None, 0, 0
        for c in chars:
            if c == pre:
                length += 1
                if length % 10 == 1 or length == 2:
                    res += 1
            else:
                pre = c
                length = 1
                res += 1
        return res

print(Solution().compress(["a","a","b","b","c","c","c"]))