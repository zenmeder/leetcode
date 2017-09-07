#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def isPalindrome(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		i = 0
		j = len(s) - 1
		while i <= j:
			if self.isAlphanumeric(s[i]) and self.isAlphanumeric(s[j]):
				if self.Equal(s[i], s[j]):
					i += 1
					j -= 1
					continue
				else:
					return False
			if not self.isAlphanumeric(s[i]):
				while i < len(s) and not self.isAlphanumeric(s[i]):
					i += 1
			if not self.isAlphanumeric(s[j]):
				while j >= 0 and not self.isAlphanumeric(s[j]):
					j -= 1
		return True
	def isAlphanumeric(self, x):
		x = x.upper()
		if '0' <= x <= '9' or 'A' <= x <= 'Z':
			return True
		return False

	def Equal(self, x, y):
		if x.upper() == y.upper():
			return True
		return False
print(Solution().isPalindrome("aba"))