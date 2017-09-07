#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
from itertools import permutations
from collections import Counter


class Solution(object):
	def checkInclusion(self, s1, s2):
		"""
		:type s1: str
		:type s2: str
		:rtype: bool
		"""
		c1 = Counter(s1)
		c2 = Counter(s2)
		c3 = Counter(s2[:len(s1)])
		for letter in c1:
			if letter not in c2 or c2[letter] < c1[letter]:
				return False
		if c3 == c1:
			return True
		for i in range(1, len(s2) - len(s1) + 1):
			c3[s2[i - 1]] -= 1
			if c3[s2[i - 1]] == 0:
				del c3[s2[i - 1]]
			if s2[len(s1) + i - 1] in c3:
				c3[s2[len(s1) + i - 1]] += 1
			else:
				c3[s2[len(s1) + i - 1]] = 1
			if c3 == c1:
				return True
		return False


print(Solution().checkInclusion("ab",
								"eidboaooo"))
