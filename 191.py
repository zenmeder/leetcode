#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def hammingWeight(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		count = 0
		for i in range(32):
			if n & 1:
				count += 1
			n>>=1
		return count


solution = Solution()
print(solution.hammingWeight(0))
