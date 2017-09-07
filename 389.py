#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def findTheDifference(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: str
		"""
		d = {}
		for i in range(len(s)):
			if s[i] in d:
				d[s[i]] += 1
			else:
				d[s[i]] = 1
		for j in range(len(t)):
			if t[j] in d:
				d[t[j]] -= 1
			if t[j] not in d or d[t[j]] == -1:
				return t[j]
