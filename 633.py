#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"
import math
class Solution(object):
	def judgeSquareSum(self, c):
		"""
		:type c: int
		:rtype: bool
		"""
		# if c==1 :
		# 	return False
		n = int(math.sqrt(c))
		if n*n == c:
			return True
		for i in range(1,n+1):
			m = int(math.sqrt(c-i*i))
			if m*m+i*i == c:
				return True
		return False

solution = Solution()
print(solution.judgeSquareSum(6))