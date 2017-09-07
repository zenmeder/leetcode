#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: List[str]
		:rtype: List[str]
		"""
		dps = []
		for i in range(len(s)):
			for j in range(i):
				if dps:
					for dp in dps[-1]:
						if 