#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def numDecodings(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		if not s:
			return 0
		dp = [0 for i in range(len(s))]
		dp[0] = 1 if '1'<=s[0]<='9' else 0
		for i in range(1, len(s)):
			m = dp[i - 2] if i >=2 else 1
			n = 1 if '10'<=s[i-1]+s[i]<='26' else 0
			p = 1 if '1'<=s[i]<='9' else 0
			dp[i] = dp[i-1]*p+m*n
		return dp[-1]

print(Solution().numDecodings('0'))
