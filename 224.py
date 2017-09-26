#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, res, stack, numstack = 0, 0, [], []
        while i < len(s):
            if not s[i]:
                continue
            if s[i] == '(':
                stack.append(s[i])
            elif '0' <= s[i] <= '9':
                numstack.append(s[i])
            elif