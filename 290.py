#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def wordPattern(self, pattern, str):
		"""
		:type pattern: str
		:type str: str
		:rtype: bool
		"""
		str = str.split()
		if len(str) != len(pattern):
			return False
		d1 = {}
		d2 = {}
		for p, s in zip(pattern, str):
			if p not in d1:
				d1[p] = s
				if s in d2 and d2[s] != p:
					return False
				d2[s] = p
			elif d1[p] != s:
				return False
		return True
