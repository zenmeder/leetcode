#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1,1]
        for i in range(2, n+1):
            tmp = 0
            for j in range(i):
                tmp += dp[j]* dp[i-j-1]
            dp.append(tmp)
        return dp[-1]

print(Solution().numTrees(3))