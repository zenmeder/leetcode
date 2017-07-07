#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def longestPalindromeSubseq(self, s):
		# a = {}
		# count = 0
		# n = len(s)
		# for i in range(n):
		# 	if s[i] in a and a[s[i]]==1:
		# 		a[s[i]] = 0
		# 		count += 2
		# 		continue
		# 	a[s[i]] = 1
		# return count if count==n else count+1

solution = Solution()
print(solution.longestPalindromeSubseq('ab'))