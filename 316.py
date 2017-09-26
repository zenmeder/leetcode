#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        letters, length= [chr(_) for _ in range(97, 123)], len(s)
        res, pre= [], float('inf')
        for letter in letters:
            position = [_ for _ in range(length) if letter == s[_]]
            if not position:
                res.append(-1)
                continue
            if len(position) == 1:
                res.append(position[0])
            else:




        return s

print(Solution().removeDuplicateLetters('cbacdcbc'))