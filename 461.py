#!/usr/local/bin/ python3
# -*- coding:utf-8 -*-
# __author__ = "zenmeder"

class Solution(object):
	def hammingDistance(self, x, y):
		"""
		:type x: int
		:type y: int
		:rtype: int
		"""
		z = x ^ y
		count = 0
		while z:
			if z & 1:
				count += 1
			z >>= 1
		return count

print(Solution().hammingDistance(4,1))
