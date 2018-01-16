#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution:
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        m, n = len(s1), len(s2)
        dp = [[0 for _ in range(n+1)] for __ in range(m+1)]
        for j in range(1, n+1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j-1])
        for i in range(1, m+1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])
            for j in range(1,n+1):
                dp[i][j] = min(ord(s1[i-1]) + dp[i - 1][j], ord(s2[j-1]) + dp[i][j - 1]) if s1[i-1]!=s2[j-1] else dp[i-1][j-1]
        return dp[-1][-1]

l = 'sj'
print(sum([ord(_) for _ in l]))
print(Solution().minimumDeleteSum("sjfqkfxqoditw", "fxymelgo"))
print(Solution().minimumDeleteSum('delete','leet'))
