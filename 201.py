#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution:
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if len(bin(m)) != len(bin(n)):
            return 0
        res = m
        for i in range(m+1, n+1):
            res &= i
        return res