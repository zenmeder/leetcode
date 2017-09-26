#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1 or not word2:
            return len(word1)+len(word2)
        dp = [[0]* len(word2) for _ in range(len(word1))]
        for i in range(len(word1)):
            for j in range(len(word2)):
                if i == 0:
                    dp[i][j] = 1 if word1[0] in word2[:j+1] else 0
                elif j == 0:
                    dp[i][j] = 1 if word2[0] in word1[:i+1] else 0
                elif word1[i] == word2[j]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return len(word1)+len(word2)-2*dp[-1][-1]

print(Solution().minDistance('a',''))