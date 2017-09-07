#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def isIsomorphic(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""
		d = {}
		for i in range(len(s)):
			if s[i] not in d:
				d[s[i]] = t[i]
			elif d[s[i]] != t[i]:
				return False
		if len(d.values()) != len(set(d.values())):
			return False
		return True

print(Solution().isIsomorphic('egd','add'))