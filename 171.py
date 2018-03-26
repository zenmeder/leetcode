#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters, res, length = {chr(_):_-64 for _ in range(65, 91)},0, len(s)
        for i in range(length):
            res += letters[s[i]] * 26 **(length-i-1)
        return res

print(Solution().titleToNumber('DY'))