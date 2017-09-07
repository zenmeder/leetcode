#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def partition(self, s):
		"""
		:type s: str
		:rtype: List[List[str]]
		"""
		res = []
		for i in range(len(s) - 1):
			if self.ifPalindrome(s[:i]) and self.ifPalindrome(s[i:]):
				res.append([s[:i], s[i:]])
		return res

	def ifPalindrome(self, s):
		if not s:
			return True
		i, j = 0, len(s) - 1
		while i <= j:
			if s[i] == s[j]:
				i += 1
				j -= 1
			else:
				return False
		return True

print(Solution().partition('aab'))