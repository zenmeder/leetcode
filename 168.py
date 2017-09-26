#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
    def convertToTitle(self, n):
        res = []
        while n > 0:
            if n % 26 == 0:
                res.append('Z')
            else:
                res.append(chr(n % 26 + 64))
            n = (n - 1) // 26
        return ''.join(res[::-1])


print(Solution().convertToTitle(26))
