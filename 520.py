#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def detectCapitalUse(self, word):
		"""
		:type word: str
		:rtype: bool
		"""
		flag1 = 0
		flag2 = 0
		flag3 = 0
		for i in range(len(word)):
			if not 'A' <= word[i] <= 'Z':
				flag1 = 1
			if not 'a' <= word[i] <= 'z':
				flag2 = 1
			if i >= 1 and not 'a' <= word[i] <= 'z':
				flag3 = 1
		if (len(word) > 1 and not flag1) or not flag2 or (len(word) > 1 and not flag3):
			return True
		return False

print(Solution().detectCapitalUse('A'))