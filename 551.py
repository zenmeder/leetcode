#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def checkRecord(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		return ('LLL' not in s) and (len(s)-len(s.replace('A','',2))<2)

solution = Solution()
print(solution.checkRecord('APDJLA'))