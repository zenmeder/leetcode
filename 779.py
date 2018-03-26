#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution:
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        flag = 1
        while N > 1:
            flag = flag if K % 2 else not flag
            K = (K+1)//2
            N -= 1
        return 0 if flag else 1
for i in range(1,9):
    print(Solution().kthGrammar(4,i))