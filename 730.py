#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution:
    def countPalindromicSubsequences(self, S):
        """
        :type S: str
        :rtype: int
        """
        length = len(S)
        dp = [[0 for _ in range(length)] for __ in range(length)]
        for i in range(length):
            for j in range(i, length):
                if i == j:
                    dp[i][j] = 1
        def next(c, i, j):
            for k in range(i, j+1):
                if S[k] == c:
                    return k
            return j + 1
        def pre(c, i, j):
            for k in range(i, j)[::-1]:
                if S[k] == c:
                    return k
            return i - 1