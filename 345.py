#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def reverseVowels(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		if not s:
			return s
		s = list(s)
		i = 0
		j = len(s) - 1
		vowels = list('aeiouAEIOU')
		while True:
			while i < len(s) and s[i] not in vowels :
				i += 1
			while j>0 and s[j] not in vowels:
				j -= 1
			if i <= j:
				s[i], s[j] = s[j], s[i]
				i += 1
				j -= 1
			else:
				break
		return ''.join(s)


print(Solution().reverseVowels('aA'))
