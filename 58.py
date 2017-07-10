#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
class Solution(object):
	def lengthOfLastWord(self, s):
		"""
		:type s: str
		:rtype: int
		"""

		s = s.split()
		if len(s) == 0:
			return 0
		return len(s[-1])

solution = Solution()
print(solution.lengthOfLastWord('    '))
