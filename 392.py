#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def isSubsequence(self, s: str, t:str) -> bool:
		i = j = 0
		while i < len(s) and j < len(t):
			if t[j] == s[i]:
				j += 1
				i += 1
			else:
				j += 1
		if i==len(s):
			return True
		return False

print(Solution().isSubsequence('abc','ahbgdc'))