#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def firstUniqChar(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		# 遍历两次
		count = {}
		for i in range(len(s)):
			if s[i] in count:
				count[s[i]] += 1
			else:
				count[s[i]] = 1
		for i in range(len(s)):
			if count[s[i]] == 1:
				return i
		return -1