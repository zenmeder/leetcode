#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p = {0}
        for i in range(len(s)):
            if s[i] == '(':
                p = {_ + 1 for _ in p}
            elif s[i] == ')':
                p = {_ - 1 for _ in p if _ > 0}
            elif s[i] == '*':
                p = p | {_ + 1 for _ in p} | {_ - 1 for _ in p if _ > 0}
            if not p:
                break
        return True if p else False

print(Solution().checkValidString("(*))"))