#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
from collections import Counter
class Solution(object):
	def canConstruct(self, ransomNote, magazine):
		"""
		:type ransomNote: str
		:type magazine: str
		:rtype: bool
		"""
		c1, c2 = Counter(ransomNote), Counter(magazine)
		for letter in c1:
			if letter in c2 and c2[letter] >= c1[letter]:
				continue
			else:
				return False
		return True

print(Solution().canConstruct('ab','a'))